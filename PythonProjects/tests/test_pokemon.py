import requests
import pytest

host = 'https://api.pokemonbattle.me:9104'
token = '177d4130f7fad084b1b2c3fae7e64a3d'

def test_status_code():
    response = requests.get(f'{host}/trainers')
    assert response.status_code == 200

def test_part_of_answer():
    response = requests.get(f'{host}/trainers', params = {'trainer_id' : 1249})
    assert response.json()['trainer_name'] == 'Максим QA'