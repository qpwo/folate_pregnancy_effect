#!/usr/bin/env python3
import os
import subprocess

os.chdir('experimento')

if not os.path.exists('uniqs.jsonl'):
    print("uniqs.jsonl not found!")
    exit(1)

with open('uniqs.jsonl', 'r') as f:
    data = f.read()

prompt = """Hey gemminiii use ONLY the provided uniqs.jsonl data to estimate whether and how much creatine and folate each improve chanceofpreg (chance of pregnancy) and chanceofbirthGivenPreg (chance of birth given pregnancy).
Calculate these metrics for each relevant group in each trial, conserve units (show your exact numerators and denominators), and summarize the overall effects of folate and creatine separately. Talk freely and think step by step."""

cmd = [os.path.expanduser('~/bin/prosimple'), prompt, f"uniqs.jsonl:\n{data}"]
res = subprocess.run(cmd, capture_output=True, text=True)

print("==== ESTIMATION RESULTS ====\n")
print(res.stdout)
