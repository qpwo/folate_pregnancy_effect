import json
import urllib.request

doi = "10.1371/journal.pmed.1004186" # example DOI from the list
url = f"https://api.unpaywall.org/v2/{doi}?email=unpaywall_test@gmail.com"

req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req, timeout=10) as response:
        data = json.loads(response.read().decode('utf-8'))
        print("Success!")
        if data.get('best_oa_location'):
            print("OA URL:", data['best_oa_location'].get('url_for_pdf'))
except Exception as e:
    print("Error:", e)
