import json
import urllib.request
import urllib.error
import os
import concurrent.futures

def get_oa_pdf(doi):
    if not doi: return None
    url = f"https://api.unpaywall.org/v2/{doi}?email=unpaywall_test@gmail.com"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode('utf-8'))
            if data.get('best_oa_location'):
                return data['best_oa_location'].get('url_for_pdf')
    except Exception as e:
        print(f"Error checking Unpaywall for {doi}: {e}")
    return None

def download_file(url, out_path):
    if not url: return False
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=20) as response:
            content = response.read()
            # simple check that it's a PDF
            if not content.startswith(b'%PDF'):
                return False
            with open(out_path, 'wb') as f:
                f.write(content)
        return True
    except Exception as e:
        # print(f"Failed to download {url}: {e}")
        return False

results = {"creatine": [], "folate": []}
current_cat = None
with open('pubmed_results.txt', 'r') as f:
    for line in f:
        line = line.strip()
        if line.startswith("--- CREATINE ---"): current_cat = "creatine"
        elif line.startswith("--- FOLATE ---"): current_cat = "folate"
        elif line.startswith("PMID:"):
            parts = line.split(" | ")
            pmid = parts[0].replace("PMID: ", "")
            doi = parts[1].replace("DOI: ", "") if len(parts)>1 else ""
            results[current_cat].append({"pmid": pmid, "doi": doi})

def process_item(cat, item):
    doi = item['doi']
    pmid = item['pmid']
    if not doi:
        return False
    pdf_url = get_oa_pdf(doi)
    if pdf_url:
        out_path = os.path.join(cat, f"{pmid}.pdf")
        if download_file(pdf_url, out_path):
            return True
    return False

for cat, items in results.items():
    os.makedirs(cat, exist_ok=True)
    downloaded = 0
    print(f"Starting downloads for {cat} ({len(items)} items)")
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        futures = {executor.submit(process_item, cat, item): item for item in items}
        for future in concurrent.futures.as_completed(futures):
            if future.result():
                downloaded += 1
    print(f"Finished {cat}. Downloaded {downloaded}/{len(items)} PDFs.\n")
