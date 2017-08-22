import requests
r = requests.get("https://data.cityofnewyork.us/download/gua4-p9wg/application%2Fzip")
with open("nyc-east-river-bicycle-counts.zip", "wb") as f:
    f.write(r.content)
