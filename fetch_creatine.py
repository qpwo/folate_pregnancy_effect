import urllib.request, urllib.parse, json, xml.etree.ElementTree as ET, time, os, concurrent.futures, re

query = '(creatine[Title/Abstract] OR "creatine monohydrate"[Title/Abstract]) AND (pregnancy[Title/Abstract] OR pregnant[Title/Abstract] OR gestation[Title/Abstract] OR maternal[Title/Abstract]) AND "randomized controlled trial"[ptyp]'
url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term={urllib.parse.quote(query)}&retmax=100&retmode=json"

req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as resp:
    data = json.loads(resp.read().decode('utf-8'))
    pmids = data['esearchresult']['idlist']

ids = ",".join(pmids)
fetch_url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id={ids}&retmode=xml"

results = []
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
    pass

def get_oa_pdf(doi):
    if not doi: return None
    url = f"https://api.unpaywall.org/v2/{doi}?email=unpaywall_test@gmail.com"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode('utf-8'))
            if data.get('best_oa_location'): return data['best_oa_location'].get('url_for_pdf')
    except: pass
    return None

os.makedirs("creatine", exist_ok=True)
for item in results:
    doi = item['doi']
    pmid = item['pmid']
    title = item['title']
    slug = re.sub(r'[^a-zA-Z0-9]+', '_', title).strip('_')[:50]
    out_path = os.path.join("creatine", f"{pmid}_{slug}.pdf")
    pdf_url = get_oa_pdf(doi)
    if pdf_url:
        try:
            r = urllib.request.Request(pdf_url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(r, timeout=15) as response:
                content = response.read()
                if content.startswith(b'%PDF'):
                    with open(out_path, 'wb') as f: f.write(content)
        except: pass
