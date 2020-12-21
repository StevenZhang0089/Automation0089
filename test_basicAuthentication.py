import requests
from requests.auth import HTTPBasicAuth

def test_with_authernticaion():
    response = requests.get('https://api.github.com/user', auth=HTTPBasicAuth('zhe.zhang.mss@gmail.com','e3d8c956bfd7057abbbb7c49d206dffb2d1fa89f'))
    print(response.text)