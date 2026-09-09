import urllib.request
import urllib.parse
import json
import xml.etree.ElementTree as ET
import time

def search_pubmed(query):
    url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term={urllib.parse.quote(query)}&retmax=100&retmode=json"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read().decode('utf-8'))
    return data['esearchresult']['idlist']

def fetch_details(pmids):
    if not pmids:
        return []
    ids = ",".join(pmids)
    url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id={ids}&retmode=xml"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response:
        tree = ET.fromstring(response.read())

    results = []
    for article in tree.findall(".//PubmedArticle"):
        pmid = article.findtext(".//PMID")
        title = article.findtext(".//ArticleTitle")

        doi = ""
        for elId in article.findall(".//ArticleId"):
            if elId.attrib.get("IdType") == "doi":
                doi = elId.text
                break

        results.append({"pmid": pmid, "title": title, "doi": doi})
    return results

queries = {
    "creatine": '(creatine[Title/Abstract] OR "creatine monohydrate"[Title/Abstract]) AND (pregnancy[Title/Abstract] OR pregnant[Title/Abstract] OR gestation[Title/Abstract] OR maternal[Title/Abstract]) AND "randomized controlled trial"[ptyp]',
    "folate": '("folic acid"[Title/Abstract] OR folate[Title/Abstract]) AND (pregnancy[Title/Abstract] OR pregnant[Title/Abstract] OR gestation[Title/Abstract] OR maternal[Title/Abstract]) AND "randomized controlled trial"[ptyp]'
}

for name, q in queries.items():
    print(f"--- {name.upper()} ---")
    pmids = search_pubmed(q)
    print(f"Found {len(pmids)} articles for {name}")
    details = fetch_details(pmids)
    for d in details:
        print(f"PMID: {d['pmid']} | DOI: {d['doi']} | {d['title']}")
    print("")
    time.sleep(1)
