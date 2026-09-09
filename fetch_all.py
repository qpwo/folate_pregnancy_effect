import urllib.request
import urllib.parse
import json
import xml.etree.ElementTree as ET
import time
import os
import concurrent.futures
import re

query = '("folic acid"[Title/Abstract] OR folate[Title/Abstract]) AND (pregnancy[Title/Abstract] OR pregnant[Title/Abstract] OR gestation[Title/Abstract] OR maternal[Title/Abstract]) AND "randomized controlled trial"[ptyp]'
url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term={urllib.parse.quote(query)}&retmax=1000&retmode=json"

req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as resp:
    data = json.loads(resp.read().decode('utf-8'))
    pmids = data['esearchresult']['idlist']

print(f"Fetched {len(pmids)} PMIDs.")

results = []
batch_size = 200
for i in range(0, len(pmids), batch_size):
    batch = pmids[i:i+batch_size]
    ids = ",".join(batch)
    fetch_url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id={ids}&retmode=xml"

    try:
        req2 = urllib.request.Request(fetch_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req2) as resp2:
            tree = ET.fromstring(resp2.read())

            for article in tree.findall(".//PubmedArticle"):
                pmid = article.findtext(".//PMID")
                title = article.findtext(".//ArticleTitle") or "No Title"
                doi = ""
                for elId in article.findall(".//ArticleId"):
                    if elId.attrib.get("IdType") == "doi":
                        doi = elId.text
                        break
                results.append({"pmid": pmid, "title": title, "doi": doi})
    except Exception as e:
        print("Error fetching details:", e)
    time.sleep(0.5)

print(f"Fetched details for {len(results)} articles.")

def get_oa_pdf(doi):
    if not doi: return None
    url = f"https://api.unpaywall.org/v2/{doi}?email=unpaywall_test@gmail.com"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode('utf-8'))
            if data.get('best_oa_location'):
                return data['best_oa_location'].get('url_for_pdf')
    except:
        pass
    return None

def download_file(url, out_path):
    if not url: return False
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=15) as response:
            content = response.read()
            if not content.startswith(b'%PDF'): return False
            with open(out_path, 'wb') as f:
                f.write(content)
        return True
    except:
        return False

os.makedirs("folate", exist_ok=True)
downloaded = 0

def process_item(item):
    doi = item['doi']
    pmid = item['pmid']
    title = item['title']
    slug = re.sub(r'[^a-zA-Z0-9]+', '_', title).strip('_')[:50]
    out_path = os.path.join("folate", f"{pmid}_{slug}.pdf")

    # check if already exists (even with different slug)
    for existing in os.listdir("folate"):
        if existing.startswith(f"{pmid}_") and existing.endswith(".pdf"):
            return False # already have it

    if not doi: return False
    pdf_url = get_oa_pdf(doi)
    if pdf_url:
        if download_file(pdf_url, out_path):
            return True
    return False

print("Checking Unpaywall and downloading OA PDFs in parallel...")
with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
    futures = [executor.submit(process_item, item) for item in results]
    for future in concurrent.futures.as_completed(futures):
        if future.result():
            downloaded += 1

print(f"Downloaded {downloaded} new PDFs.")
