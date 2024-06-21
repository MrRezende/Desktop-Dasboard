import requests
import json

link = "https://bookify-5aa13-default-rtdb.firebaseio.com/"
requisicao = requests.get(f'{link}/.json')
print(requisicao)
print(requisicao.text)