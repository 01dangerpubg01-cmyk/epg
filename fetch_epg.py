import os
import requests
import gzip
import io

url = os.environ["EPG_SOURCE_URL"]

headers = {
    "User-Agent": "Mozilla/5.0"
}

r = requests.get(url, headers=headers, timeout=120)
r.raise_for_status()

data = r.content

# gzip auto extract
if data[:2] == b"\x1f\x8b":
    data = gzip.GzipFile(fileobj=io.BytesIO(data)).read()

text = data.decode("utf-8", errors="ignore")

if "<tv" not in text or "<channel" not in text:
    raise Exception("Invalid XMLTV file")

with open("epg.xml", "w", encoding="utf-8") as f:
    f.write(text)

print("Valid XMLTV saved")
