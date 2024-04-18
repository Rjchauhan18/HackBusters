import requests

search="monkey"
limit=20
sortField="rank"
sortInterval="1day"
Direction="ASC"

url = f"https://api.verbwire.com/v1/nft/data/collections/search?searchString={search}&limit={limit}&page=1&sortField={sortField}&sortInterval={sortInterval}&sortDirection={Direction}"

headers = {
    "accept": "application/json",
    "X-API-Key": "sk_live_bb929bd1-aabf-466e-b996-434d60d3f2bb"
}

response = requests.get(url, headers=headers)
data=response.json()
# print(data)
# print(data['collections']['results'][0])

for res in data['collections']['results']:
    for key, value in res.items():
        print(f"{key} <:====:>  {value}")
    print("\n\n\n")