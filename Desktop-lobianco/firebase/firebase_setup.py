import firebase_admin
from firebase_admin import credentials
import requests
import json

# def initialize_firebase():
#     cred = credentials.Certificate("assets/credentials.json")
#     firebase_admin.initialize_app(cred, {
#         'databaseURL': 'https://bookify-5aa13-default-rtdb.firebaseio.com/'
#     })


#Esta função faz a conexao com o firebase
def link_bd():
  link = "https://bookify-5aa13-default-rtdb.firebaseio.com/"