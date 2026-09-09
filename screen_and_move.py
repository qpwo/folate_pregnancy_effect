#!/usr/bin/env python3
import concurrent.futures
import json
import os
import subprocess
import time
import shutil

START = time.monotonic()
DIRECTORIES = ('folate', 'creatine', 'folate_rcts', 'creatine_rcts', 'pdfs')

PROMPT = """Is this paper a randomized controlled experiment involving folate or creatine in pregnancy?
Talk freely and think step by step.
At the very end of your response, output a single JSON object with exactly one key "folder" mapping to either "experimento" (if it is a relevant human RCT) or "elso" (if it is not)."""

os.makedirs('experimento', exist_ok=True)
os.makedirs('elso', exist_ok=True)

def log(msg):
    print(f"+{time.monotonic() - START:.1f} {msg}", flush=True)

def process(path):
    try:
        content = open(path, 'r', encoding='utf-8', errors='ignore').read()
    except Exception as e:
        return path, None, str(e)

    cmd = [os.path.expanduser('~/bin/prosimple'), PROMPT, f"filename: {path}\n{content}"]
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, timeout=400, start_new_session=True)
        if res.returncode != 0:
            return path, None, f"RC {res.returncode}: {res.stderr.strip()}"

        out = res.stdout.strip()
        start = out.rfind('{')
        end = out.rfind('}')
        if start != -1 and end != -1 and start < end:
            try:
                data = json.loads(out[start:end+1])
                folder = data.get('folder', 'elso')
                if folder not in ('experimento', 'elso'):
                    folder = 'elso'

                # Move .md
                shutil.move(path, os.path.join(folder, os.path.basename(path)))
                # Move associated .pdf if it exists
                pdf_path = path[:-3] if path.endswith('.md') else path
                if os.path.exists(pdf_path):
                    shutil.move(pdf_path, os.path.join(folder, os.path.basename(pdf_path)))
                # Move associated .xml if it exists
                xml_path = path[:-7] + '.xml' if path.endswith('.pdf.md') else None
                if xml_path and os.path.exists(xml_path):
                    shutil.move(xml_path, os.path.join(folder, os.path.basename(xml_path)))

                return path, folder, None
            except Exception as e:
                return path, None, f"JSON parse error: {e}"
        return path, None, "No {...} found"
    except subprocess.TimeoutExpired:
        return path, None, "Timeout"
    except Exception as e:
        return path, None, str(e)

paths = [os.path.join(d, n) for d in DIRECTORIES if os.path.isdir(d) for n in os.listdir(d) if n.endswith('.md')]
log(f"Starting {len(paths)} files")

with concurrent.futures.ThreadPoolExecutor(max_workers=10) as pool:
    futs = {pool.submit(process, p): p for p in paths}
    for fut in concurrent.futures.as_completed(futs):
        p, f, err = fut.result()
        if err:
            log(f"FAIL {p} {err}")
        else:
            log(f"MOVED {p} -> {f}")

log("Done.")
