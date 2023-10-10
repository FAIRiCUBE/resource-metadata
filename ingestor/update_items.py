import requests
import os
import pystac
from requests.auth import HTTPBasicAuth

username = os.environ["USERNAME"]
password = os.environ["PASSWORD"]

urls = [
    {
        "catalog": "https://fairicube.github.io/resource-metadata/ml_items/catalog.json",
        "api": "https://stacapi-write.eoxhub.fairicube.eu/collections/ML collection/items"
    }, {
        "catalog": "https://fairicube.github.io/resource-metadata/no-ml_items/catalog.json",
        "api": "https://stacapi-write.eoxhub.fairicube.eu/collections/no-ML collection/items"
    }
]


def cleanup_items(url, catalog_items_list):
    api_items = requests.get(url=f"{url}?limit=1000",
                             auth=HTTPBasicAuth(username, password)).json()

    # check if the already ingested items are in the catalog,
    # otherwise delete them
    if "features" in api_items.keys():
        for item in api_items["features"]:
            if item["id"] not in catalog_items_list:
                response = requests.delete(
                    url=f"{url}/{item['id']}",
                    auth=HTTPBasicAuth(username, password))
    return response.status_code


def update_collection(catalog_url, post_url):

    index_catalog = requests.get(catalog_url).json()
    catalog = pystac.Catalog.from_dict(index_catalog)
    catalog_items = catalog.get_items()

    catalog_items_list = []

    for item in catalog_items:
        catalog_items_list.append(item.id)

    for link in index_catalog["links"]:
        if link["rel"] == "item":
            json_body = requests.get(link["href"]).json()
            response = requests.post(
                url=post_url, json=json_body,
                auth=HTTPBasicAuth(
                    username, password))
            if response.status_code == 409:
                put_url = f'{post_url}/{json_body["id"]}'
                response = requests.put(
                    url=put_url, json=json_body,
                    auth=HTTPBasicAuth(
                        username, password))
            print(response, json_body["id"])


for collection in urls:
    # delete items which was removed from the catalog
    catalog_items_list = []
    index_catalog = requests.get(collection["catalog"]).json()
    catalog = pystac.Catalog.from_dict(index_catalog)
    catalog_items = catalog.get_items()

    for item in catalog_items:
        catalog_items_list.append(item.id)
    cleanup_items(collection["api"], catalog_items_list)
    update_collection(collection["catalog"], collection["api"])
