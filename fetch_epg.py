import os
import io
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

data = r.content

# Auto unzip if source is gzipped

if data[:2] == b"\x1f\x8b":
data = gzip.GzipFile(fileobj=io.BytesIO(data)).read()

text = data.decode("utf-8", errors="ignore")

if "<tv" not in text:
raise Exception("Invalid XMLTV file")

with open("epg.xml", "w", encoding="utf-8") as f:
f.write(text)

print("EPG Updated")
