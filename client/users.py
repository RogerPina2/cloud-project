import requests
from datetime import datetime

file = open('url', 'r')
lburl = file.readline().lower()
url = 'http://' + lburl

headers = {"Content-type": "application/json"}

def read_users():
    response = requests.get('{}/users/'.format(url))
    print(response.text)

def read_user(id):
    response = requests.get('{}/users/{}'.format(url, id))
    print(response.text)

def create_user(name, city, state, country):
    json={
        'name': name, 
        'city': city, 
        'state': state,
        'country': country
    }

    response = requests.post('{}/users/'.format(url), json=json, headers=headers)

    print(response.text)

def update_user(id, name, city, state, country):
    json={
        'name': name, 
        'city': city, 
        'state': state,
        'country': country
    }
    
    response = requests.put('{}/users/{}/'.format(url, id), json=json, headers=headers)
    print(response.text)

def delete_user(id):
    try:
        response = requests.delete('{}/users/{}'.format(url, id))
        print('user {} deleted'.format(id))
    except:
        print('Error')
