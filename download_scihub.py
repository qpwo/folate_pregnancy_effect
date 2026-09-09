import urllib.request
import os
import re
import concurrent.futures

SH_DOMAINS = ["https://sci-hub.st", "https://sci-hub.ru"]

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
            if doi:
                results[current_cat].append({"pmid": pmid, "doi": doi})

def get_sh(doi, pmid, cat):
    out_path = os.path.join(cat, f"{pmid}.pdf")
    if os.path.exists(out_path):
        return True # already downloaded

    for domain in SH_DOMAINS:
        try:
            url = f"{domain}/{doi}"
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
            with urllib.request.urlopen(req, timeout=10) as response:
                html = response.read().decode('utf-8', errors='ignore')

            # look for the pdf embed or iframe
            match = re.search(r"<iframe[^>]*src=[\"']([^\"']+)[\"']", html, re.IGNORECASE)
            if not match:
                match = re.search(r"<embed[^>]*src=[\"']([^\"']+)[\"']", html, re.IGNORECASE)
            if not match:
                match = re.search(r"onclick=[\"']location\.href=['\"]([^\"']+pdf[^\"']*)['\"]", html, re.IGNORECASE)

            if match:
                pdf_url = match.group(1)
                if pdf_url.startswith("//"): pdf_url = "https:" + pdf_url
                elif pdf_url.startswith("/"): pdf_url = domain + pdf_url

                req_pdf = urllib.request.Request(pdf_url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
                with urllib.request.urlopen(req_pdf, timeout=20) as pdf_resp:
                    content = pdf_resp.read()
                    if content.startswith(b'%PDF'):
                        with open(out_path, 'wb') as f:
                            f.write(content)
                        return True
        except Exception as e:
            pass
    return False

for cat, items in results.items():
    print(f"Starting Sci-Hub for {cat} ({len(items)} items)")
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        futures = {executor.submit(get_sh, item['doi'], item['pmid'], cat): item for item in items}
        for future in concurrent.futures.as_completed(futures):
            pass

    existing = len([f for f in os.listdir(cat) if f.endswith('.pdf')]) if os.path.exists(cat) else 0
    print(f"Finished {cat}. Total PDFs now present: {existing}/{len(items)}.\n")
