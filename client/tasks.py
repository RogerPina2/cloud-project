import requests
from datetime import datetime

file = open('url', 'r')
lburl = file.readline().lower()
url = 'http://' + lburl

headers = {"Content-type": "application/json"}

def read_tasks():
    response = requests.get('{}/tasks/'.format(url))
    print(response.text)

def read_task(id):
    response = requests.get('{}/tasks/{}'.format(url, id))
    print(response.text)

def create_task(title, description):

    json={
        'title': title, 
        'pub_date': str(datetime.now()), 
        'description': description
    }

    response = requests.post('{}/tasks/'.format(url), json=json, headers=headers)

    print(response.text)

def update_task(id, title, description):
    json={
        'title': title, 
        'pub_date': str(datetime.now()), 
        'description': description
    }
    
    response = requests.put('{}/tasks/{}/'.format(url, id), json=json, headers=headers)
    print(response.text)

def delete_task(id):
    try:
        response = requests.delete('{}/tasks/{}'.format(url, id))
        print('task {} deletad'.format(id))
    except:
        print('Error')
