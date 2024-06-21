from firebase_admin import db
from firebase_setup import link_bd
import requests
import json

# def get_data(path):
#     ref = db.reference(path)
#     return ref.get()


#Esta função faz a quisição dos dados
def get_data():
    requisicao = requests.get(f'{link_bd}/.json')