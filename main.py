import time
from datetime import datetime, timezone

import requests

URL = "https://obs.itu.edu.tr/api/ders-kayit/v21"
headers = {
    "Authorization": "",
    "Cookie": "",
    "Content-Type": "application/json",
    "Charset": "utf-8",
    "Path": "/api/ders-kayit/v21",
    "Authority": "kepler-beta.itu.edu.tr",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Scheme": "https",
    "Date": None,
}

headers["Authorization"] = input("Authorization: ")
headers["Cookie"] = input("Cookie: ")

payload = {
    "ECRN": [
        # Database Systems
        "13594",
        "13593",
        # EHB
        "10099",
        "10958",
        # Rus 3
        "10617",
        # ITB
        "12933",
        "12910",
        "12838",
        "12863",
        "12915",
        "12830",
        # SNT
        "10548",
    ],
    "SCRN": ["13593", "10958"],
}

while True:
    headers["Date"] = datetime.now(timezone.utc).strftime("%a, %d %b %Y %H:%M:%S GMT")
    response = requests.post(URL, json=payload, headers=headers)
    print("\n\n", response.status_code, response.text, "\n\n")
    time.sleep(0.5)
