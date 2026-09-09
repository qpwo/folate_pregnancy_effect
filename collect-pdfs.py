#!/usr/bin/env python3
import concurrent.futures
import json
import os
import subprocess
import time

selected = {
    "folate": """PMC6133042 PMC4668025 PMC3635165 PMC1617124 PMC11574634
PMC11547940 PMC11869910 PMC8106758 PMC6503513 PMC6529553 PMC5221122
PMC5331770 PMC5439041 PMC6823954 PMC6380035 PMC7945668 PMC11650848
PMC7551257 PMC4515996 PMC11003863 PMC10338559 PMC11032415 PMC1700896
PMC1912617 PMC1944952 PMC476777 PMC1793975 PMC1505459 PMC151518""".split(),
    "creatine": """PMC11889532 PMC11871691 PMC4773130 PMC10097948
PMC9542404 PMC6770830 PMC3745711""".split(),
}
records = {}
for compound in selected:
    for row in json.load(open(compound + "-database.json"))["resultList"]["result"]:
        if row.get("pmcid") in selected[compound]:
            records[row["pmcid"]] = dict(row, compound=compound)
for pmcid in selected["folate"]:
    records.setdefault(pmcid, {"pmcid": pmcid, "compound": "folate", "title": "See primary-papers.txt"})
start = time.monotonic()

def fetch(row):
    pmcid = row["pmcid"]
    path = f"pdfs/{pmcid}.pdf"
    url = f"https://europepmc.org/articles/{pmcid}?pdf=render"
    print(f"{time.strftime('%FT%T')} start {pmcid}", flush=True)
    if os.path.exists(path):
        body = open(path, "rb").read()
    else:
        result = subprocess.run(["curl", "-fLSs", "--max-time", "40", url], stdout=subprocess.PIPE)
        body = result.stdout
    valid = body.startswith(b"%PDF-") and b"%%EOF" in body[-4096:]
    if valid and not os.path.exists(path):
        with open(path, "xb") as out:
            out.write(body)
    outcome = dict(pmcid=pmcid, compound=row["compound"], title=row["title"],
                   doi=row.get("doi"), url=url, path=path if valid else None,
                   status="pdf-downloaded-screening-pending" if valid else "download-failed")
    print(f"{time.strftime('%FT%T')} {outcome['status']} {pmcid} bytes={len(body)}", flush=True)
    time.sleep(2)
    return outcome

outcomes = []
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
    pending = {pool.submit(fetch, row) for row in records.values()}
    while pending:
        completed, pending = concurrent.futures.wait(pending, timeout=10, return_when=concurrent.futures.FIRST_COMPLETED)
        for future in completed:
            outcomes.append(future.result())
        print(f"{time.strftime('%FT%T')} found={len(records)} done={len(outcomes)} remaining={len(pending)}", flush=True)
with open("download-manifest.json", "w") as out:
    json.dump(outcomes, out, indent=2)
print(f"Elapsed={time.monotonic()-start:.1f}s PDFs={sum(bool(row['path']) for row in outcomes)}")
