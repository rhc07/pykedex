import requests
import json

BASE_URL = "https://pokeapi.co"


def query_pokeapi(resource_url):
    url = "{0}{1}".format(BASE_URL, resource_url)
    response = requests.get(url)

    if response.status_code == 200:
        return json.loads(response.text)
    return None


charizard = query_pokeapi("/api/v1/pokemon/charizard/")

sprite_uri = charizard["sprites"]["other"]["dream_world"]["front_default"]


print(charizard["name"])
print(sprite_uri)
