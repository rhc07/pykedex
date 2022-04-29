import requests
import json

BASE_URL = "https://pokeapi.co/api/v1/pokemon/"


def get_pokemon():
    pokemon = input("Please choose a pokemon:\n")
    print(pokemon)
    query_pokeapi(pokemon)


def query_pokeapi(pokemon):
    url = "{0}{1}".format(BASE_URL, pokemon)
    response = requests.get(url)

    if response.status_code == 200:
        data = json.loads(response.text)
        name = data["name"]
        picture = data["sprites"]["other"]["dream_world"]["front_default"]
        print(name)
        print(picture)
    else:
        print("An error occurred querying API")


get_pokemon()
