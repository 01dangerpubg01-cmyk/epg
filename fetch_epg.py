import os
import io
import gzip
import requests

url = os.environ["EPG_SOURCE_URL"]

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/125.0 Safari/537.36",
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate"
}

r = requests.get(
    url,
    headers=headers,
    timeout=120,
    allow_redirects=True
)

print("HTTP Status:", r.status_code)

r.raise_for_status()

data = r.content

# gzip magic bytes check
if data[:2] == b"\x1f\x8b":
    print("GZIP detected, extracting...")
    data = gzip.GzipFile(
        fileobj=io.BytesIO(data)
    ).read()

# XML validation
text = data.decode("utf-8", errors="ignore")

if "<tv" not in text:
    raise Exception("Invalid XMLTV content received")

# Save plain XML
with open("epg.xml", "w", encoding="utf-8") as f:
    f.write(text)

# Also save compressed version
with gzip.open("epg.xml.gz", "wb") as gz:
    gz.write(text.encode("utf-8"))

print("EPG Updated Successfully")
