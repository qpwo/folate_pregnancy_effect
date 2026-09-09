#!/usr/bin/env python3
import json
import math

trials = []
with open('experimento/uniqs.jsonl') as f:
    for line in f:
        trials.append(json.loads(line))

def is_control(d):
    d = d.lower()
    return any(x in d for x in ['placebo', 'excluding folic', 'trace elements'])

def is_folate(d):
    d = d.lower()
    if is_control(d): return False
    return any(x in d for x in ['folic', 'folate', '5-mthf', 'vitamins'])

ors = []

print("papername is the name of the trial; f_happy and f_fail are the counts of successful and failed pregnancies in the folate group; c_happy and c_fail are the corresponding counts in the control group; f_happy/f_fail and c_happy/c_fail are their respective odds (with +0.5 pseudocounts applied for stability); and folate_better_factor is the odds ratio of the two.")
print(f"{'papername':<55} | {'f_happy':<7} | {'f_fail':<6} | {'c_happy':<7} | {'c_fail':<6} | {'f_happy/f_fail':<14} | {'c_happy/c_fail':<14} | {'folate_better_factor':<20}")
print("-" * 155)

for t in trials:
    arms = t.get('best_data', [])
    if any(is_control(a['description']) for a in arms) and any(is_folate(a['description']) for a in arms) and any('numpregfinishiohappy' in a for a in arms):

        c_baby = c_preg = 0
        f_baby = f_preg = 0

        for a in arms:
            if 'numpregfinishiohappy' not in a: continue
            baby = a['numpregfinishiohappy']
            preg = a.get('numpregstart', a.get('numlady', baby))

            if is_control(a['description']):
                c_baby += baby; c_preg += preg
            elif is_folate(a['description']):
                f_baby += baby; f_preg += preg

        f_failed = f_preg - f_baby
        c_failed = c_preg - c_baby

        if f_preg > 0 and c_preg > 0:
            # Add 0.5 to numerator and denominator to prevent division by zero (Haldane-Anscombe)
            f_odds = (f_baby + 0.5) / (f_failed + 0.5)
            c_odds = (c_baby + 0.5) / (c_failed + 0.5)
            or_val = f_odds / c_odds
            ors.append(or_val)

            print(f"{t['experiment_name']:<55} | {f_baby:<7} | {f_failed:<6} | {c_baby:<7} | {c_failed:<6} | {f_odds:<14.4f} | {c_odds:<14.4f} | {or_val:<20.4f}")

def geomean(vals):
    if not vals: return 0
    return math.exp(sum(math.log(v) for v in vals) / len(vals))

print("-" * 155)
print(f"{'Product':<119} | {math.prod(ors):<20.4f}")
print(f"{'Geometric Mean':<119} | {geomean(ors):<20.4f}")
