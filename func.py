import requests


def request():
    response = requests.get('http://127.0.0.1:5000/')
    return response.text


request()
