import os
import gzip
import requests

url = os.environ["EPG_SOURCE_URL"]

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/125.0 Safari/537.36",
    "Accept": "*/*"
}

r = requests.get(
    url,
    headers=headers,
    timeout=120,
    allow_redirects=True
)

print("Status:", r.status_code)

r.raise_for_status()

with gzip.open("epg.xml.gz", "wb", compresslevel=9) as gz:
    gz.write(r.content)

print("EPG Updated")
