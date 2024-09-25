import requests
token = 'a3885fe83f63ca12849bcc4241b29488'
host = 'https://api.pokemonbattle.ru/v2'
'''response_add_pokemon = requests.post(f'{host}/pokemons', json = {
    "name": "python",
    "photo_id": "92"
}, headers = {'Content-Type' : 'application/json', 'trainer_token': token})

print(response_add_pokemon.text)'''

'''responce_change = requests.put(f'{host}/pokemons', json = {
    "pokemon_id": "75029",
    "name": "nohtyp",
    "photo_id": "92"
}, headers = {'Content-Type' : 'application/json' , 'trainer_token' : 
              token } )

print(responce_change.text)'''

'''responce_gacha = requests.post(f'{host}/trainers/add_pokeball', json = {
    "pokemon_id": "75029"
}, headers = {'Content-Type' : 'application/json' , 'trainer_token' : 
              token } )

print(responce_gacha.text)'''