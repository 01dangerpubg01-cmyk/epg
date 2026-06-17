import os
import requests

url = os.environ["EPG_SOURCE_URL"]

headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "*/*"
}

print("URL exists:", bool(url))
print("URL length:", len(url))

r = requests.get(
    url,
    headers=headers,
    timeout=120,
    allow_redirects=True
)

print("Status:", r.status_code)
print(r.text[:300])

r.raise_for_status()

with open("epg.xml", "wb") as f:
    f.write(r.content)
