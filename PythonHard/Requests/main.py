import requests 
 
URL = 'https://api.pokemonbattle.ru/v2' 
TOKEN =  'cfed23a4098a31990d18531a46bedd77'
HEADER = {'Content-Type':'application/json','trainer_token':TOKEN} 

body_create = {
    "name": "Hard21",
    "photo": -1
}

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
#print(response_create.text)

pokemon_id = response_create.json()['id']
print(pokemon_id)

body_name_change = {
    "pokemon_id": pokemon_id, 
    "name": "generate",
    "photo_id": -1
}

response_name_change = requests.put(url=f'{URL}/pokemons', headers = HEADER, json = body_name_change)
print(response_name_change.text)

pokemon_name = response_name_change.json()['message']
print(pokemon_name)

body_add_pokeball ={
    "pokemon_id": pokemon_id
}

response_add_pokeball = requests.post(url=f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add_pokeball)
print(response_add_pokeball.text)

add_pokeball = response_add_pokeball.json()['message']
print(add_pokeball)