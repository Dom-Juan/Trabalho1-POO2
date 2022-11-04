import PySimpleGUI as sg
import sys
import json

# import de classes
sys.path.append('../')
from classes.user.user_client import UserClient
from classes.user.user_broker import UserBroker
from classes.property.residential_apartment import  ResidentialApartment
from os import path
from pathlib import Path

# Lógica de salvar dados em JSON
def save_to_file(list) -> True:
  todo = "TODO"
  print(todo)
  return True

# FIM Lógica de salvar dados em JSON