import os
import requests

url = os.environ["EPG_SOURCE_URL"]

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/125.0 Safari/537.36",
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "keep-alive"
}

r = requests.get(
    url,
    headers=headers,
    timeout=120,
    allow_redirects=True
)

print("Status:", r.status_code)

if r.status_code != 200:
    print(r.text[:500])

r.raise_for_status()

with open("epg.xml", "wb") as f:
    f.write(r.content)

print("EPG Updated")
