import os
import gzip
import requests

url = os.environ["EPG_SOURCE_URL"]

r = requests.get(url, timeout=120)
r.raise_for_status()

with gzip.open("epg.xml.gz", "wb", compresslevel=9) as gz:
    gz.write(r.content)

print("EPG Updated")
