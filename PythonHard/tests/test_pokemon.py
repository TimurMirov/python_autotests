import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2' 
TOKEN = 'cfed23a4098a31990d18531a46bedd77' 
HEADER = {'Content-Type':'application/json','trainer_token':TOKEN} 
TRAINER_ID = 7379

def test_status_code():
    response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' :TRAINER_ID})
    assert response.status_code ==200

def test_part_of_response():
    response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id' :TRAINER_ID})
    assert response_get.json()['data'][0]['trainer_name'] == 'Атлант'