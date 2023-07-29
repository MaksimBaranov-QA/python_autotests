import requests

host = 'https://api.pokemonbattle.me:9104'
token = '177d4130f7fad084b1b2c3fae7e64a3d'

'''response_add_pokemon = requests.post(f'{host}/pokemons',json = {
    "name": "Макруша",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}, headers = {'Content-Type' : 'application/json',
             'trainer_token' : token} )

print(response_add_pokemon.json())'''

'''response_name_pokemon = requests.put(f'{host}/pokemons',json = {
    "pokemon_id": "5602",
    "name": "Валенок",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}, headers = {'Content-Type' : 'application/json',
             'trainer_token' : token} )

print(response_name_pokemon.json())'''

response_pokemon_pokeboll = requests.post(f'{host}/trainers/add_pokeball',json = {
    "pokemon_id": "5602"
}, headers = {'Content-Type' : 'application/json',
             'trainer_token' : token} )

print(response_pokemon_pokeboll.json())