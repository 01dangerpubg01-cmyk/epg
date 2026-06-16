import os
import requests

url = os.environ["EPG_SOURCE_URL"]

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/125.0 Safari/537.36",
    "Accept": "*/*"
}

response = requests.get(
    url,
    headers=headers,
    timeout=120,
    allow_redirects=True
)

print("Status Code:", response.status_code)

response.raise_for_status()

with open("epg.xml", "wb") as f:
    f.write(response.content)

print("EPG saved as epg.xml")
