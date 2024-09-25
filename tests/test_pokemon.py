import requests
import pytest

host = 'https://api.pokemonbattle.ru/v2'
trainer_id = '5954'

def test_status_code():
    response = requests.get(f'{host}/trainers', params={'trainer_id': trainer_id})
    assert response.status_code == 200

def test_part_of_answer():
    response = requests.get(f'{host}/trainers', params={'trainer_id': trainer_id})
    assert response.status_code == 200 
    data = response.json()['data'][0] 
    assert data['trainer_name'] == 'Крекозябр'
