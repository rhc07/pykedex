import requests
import json

BASE_URL = "https://pokeapi.co/api/v1/pokemon/"


def get_pokemon():
    pokemon = input("Please choose a pokemon (name or ID):\n")
    print(pokemon)
    # TODO: error handle - use regex to check if string is a number to parse id
    if pokemon == "":
        print("please try again!")
        get_pokemon()
    elif len(pokemon) > 11:
        print("too many characters in the pokemon's name or id, please try again!")
        get_pokemon()
    else:
        query_pokeapi(pokemon.lower())


def query_pokeapi(pokemon):
    url = "{0}{1}".format(BASE_URL, pokemon)
    response = requests.get(url)

    if response.status_code == 200:
        data = json.loads(response.text)
        name = str(data["name"])
        picture = data["sprites"]["other"]["dream_world"]["front_default"]
        print(name.title())
        print(picture)
    else:
        print("Pokemon doesn't exist")


get_pokemon()
