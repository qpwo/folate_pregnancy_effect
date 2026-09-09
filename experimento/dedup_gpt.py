#!/usr/bin/env python3
import os
import json
import subprocess

os.chdir('experimento')

with open('exprmnt.jsonl', 'r') as f:
    records = [json.loads(l) for l in f if l.strip()]

prompt = """I have extracted pregnancy outcome data from various files. Some files are duplicates or refer to the exact same trial (e.g., same authors, same population, same decade).
Please process this list and output a JSON object with three keys:
1. "ruff": A list of the original objects that are rough, vague, or seem broken (e.g., weird group descriptions, missing numbers).
2. "clearcut": A list of the original objects that have clear, well-defined group data.
3. "uniqs": A list of unique experiments derived from the "clearcut" list. For each unique experiment, group the duplicates together. Return an object with:
    - "experiment_name": A short name for the trial
    - "exact_filenames_included": A list of filenames that are duplicates for this trial
    - "best_data": The "groups" array from the best representative file.

Output ONLY the JSON object. Do not include markdown formatting or fences."""

print("Sending data to GPT-5.6 Sol...")
cmd = [os.path.expanduser('~/bin/56ssimple'), prompt, json.dumps(records)]
res = subprocess.run(cmd, capture_output=True, text=True)

if res.returncode != 0:
    print("Error calling 56ssimple:", res.stderr)
    exit(1)

out = res.stdout.strip()
try:
    start = out.find('{')
    end = out.rfind('}')
    data = json.loads(out[start:end+1])

    with open('ruff.jsonl', 'w') as f:
        for item in data.get('ruff', []):
            f.write(json.dumps(item) + '\n')

    with open('clearcut.jsonl', 'w') as f:
        for item in data.get('clearcut', []):
            f.write(json.dumps(item) + '\n')

    with open('uniqs.jsonl', 'w') as f:
        for item in data.get('uniqs', []):
            f.write(json.dumps(item) + '\n')

    print(f"Created ruff.jsonl ({len(data.get('ruff', []))}), clearcut.jsonl ({len(data.get('clearcut', []))}), and uniqs.jsonl ({len(data.get('uniqs', []))})")

except Exception as e:
    print("Failed to parse JSON from output.")
    print("Output was:", out)
    print("Error:", e)
