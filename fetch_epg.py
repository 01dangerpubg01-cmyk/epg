import os
import io
import gzip
import requests

url = os.environ["EPG_SOURCE_URL"]

headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "*/*"
}

r = requests.get(
    url,
    headers=headers,
    timeout=120,
    allow_redirects=True
)

r.raise_for_status()

data = r.content

# Auto extract gzip if needed
if data[:2] == b"\x1f\x8b":
    data = gzip.GzipFile(
        fileobj=io.BytesIO(data)
    ).read()

with open("epg.xml", "wb") as f:
    f.write(data)

print("EPG Updated")
