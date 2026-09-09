#!/usr/bin/env python3
import os
import json
import subprocess
import concurrent.futures
import time

os.chdir('experimento')
files = [f for f in os.listdir('.') if f.endswith('.md')]

PROMPT = """You are extracting pregnancy outcome data from randomized controlled trials of folate or creatine.
Talk freely and think step by step.
At the very end of your response, output a single JSON object.
If the paper contains group-level data on pregnancies and birth outcomes, output:
{
  "exact_filename": "<the filename you were given>",
  "groups": [
    {
      "description": "<description of the intervention/control group>",
      "numlady": <number of women randomized to this group>,
      "numpregstart": <number of pregnancies in this group>,
      "numpreg12week": <number of pregnancies continuing past 12 weeks, if available>,
      "numpregfinishiohappy": <number of live births or healthy babies, if available>
    }
  ]
}
Omit columns (keys) that are not applicable or not reported.
If the paper is just a protocol, a follow-up of children years later without group sizes for the original birth outcomes, or otherwise doesn't contain useful data on pregnancy rates/birth rates, output:
{
  "exact_filename": "<filename>",
  "unapplicable": true,
  "reason": "..."
}
Make sure the JSON is the very last thing you output."""

print(f"Extracting data from {len(files)} files in experimento...")

def process(f):
    content = open(f, 'r', encoding='utf-8', errors='ignore').read()
    cmd = [os.path.expanduser('~/bin/prosimple'), PROMPT, f"filename: {f}\n{content}"]
    res = subprocess.run(cmd, capture_output=True, text=True)
    out = res.stdout.strip()
    end = out.rfind('}')
    if end != -1:
        depth = 0
        start = -1
        for i in range(end, -1, -1):
            if out[i] == '}':
                depth += 1
            elif out[i] == '{':
                depth -= 1
            if depth == 0:
                start = i
                break
        if start != -1:
            try:
                return json.loads(out[start:end+1])
            except Exception as e:
                return {"exact_filename": f, "error": f"json parse failed: {e}", "raw": out[start:end+1]}
    return {"exact_filename": f, "error": "no json found", "raw": out[-200:]}

with open('exprmnt.jsonl', 'w') as f_exp, open('other.jsonl', 'w') as f_oth:
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as pool:
        for data in pool.map(process, files):
            if data.get('unapplicable') or 'error' in data:
                f_oth.write(json.dumps(data) + '\n')
            else:
                f_exp.write(json.dumps(data) + '\n')
            f_oth.flush()
            f_exp.flush()
            print(f"Processed {data.get('exact_filename')}")

print("Extraction complete.")
