import json, urllib.request, urllib.parse, os, re

def get_count(query):
    url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term={urllib.parse.quote(query)}&retmax=1&retmode=json"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            return int(data['esearchresult']['count'])
    except Exception as e:
        print("Count error:", e)
        return 0

queries = {
    "creatine": '(creatine[Title/Abstract] OR "creatine monohydrate"[Title/Abstract]) AND (pregnancy[Title/Abstract] OR pregnant[Title/Abstract] OR gestation[Title/Abstract] OR maternal[Title/Abstract]) AND "randomized controlled trial"[ptyp]',
    "folate": '("folic acid"[Title/Abstract] OR folate[Title/Abstract]) AND (pregnancy[Title/Abstract] OR pregnant[Title/Abstract] OR gestation[Title/Abstract] OR maternal[Title/Abstract]) AND "randomized controlled trial"[ptyp]'
}

print("Total Creatine RCTs on PubMed:", get_count(queries['creatine']))
print("Total Folate RCTs on PubMed:", get_count(queries['folate']))

pmid_to_title = {}
if os.path.exists('pubmed_results.txt'):
    with open('pubmed_results.txt', 'r') as f:
        for line in f:
            if line.startswith("PMID:"):
                parts = line.strip().split(" | ")
                pmid = parts[0].replace("PMID: ", "")
                title = parts[-1]
                pmid_to_title[pmid] = title

if os.path.exists("folate"):
    for f in os.listdir("folate"):
        if f.endswith(".pdf") and not "_" in f:
            pmid = f.replace(".pdf", "")
            if pmid in pmid_to_title:
                title = pmid_to_title[pmid]
                slug = re.sub(r'[^a-zA-Z0-9]+', '_', title).strip('_')[:50]
                new_name = f"{pmid}_{slug}.pdf"
                os.rename(os.path.join("folate", f), os.path.join("folate", new_name))
                print(f"Renamed {f} to {new_name}")
