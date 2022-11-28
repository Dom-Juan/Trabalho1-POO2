import PySimpleGUI as sg
import sys
import json

from gui.gui_create_obj import create_insurance_from_file, create_property_from_file, create_sale_from_file, \
  create_user_from_file

# import de classes
sys.path.append('../')
from os import path
from pathlib import Path


# Mensagem de sucesso
def result_window(text) -> None:
  layout = [
    [sg.Text(text, key="new")],
    [sg.Button('Ok', pad=(5, 5), size=(20, 1))]
  ]
  window = sg.Window("Alerta!", layout, size=(320, 120), element_justification='c', resizable=True, modal=True)
  while True:
    event, values = window.read(close=True)
    if event in ["Exit", sg.WIN_CLOSED, "Ok"]:
      break
  window.close()

# Lógica de carregar arquivos
# Usuários
def load_file_gui_users():
  layout = [
    [
      sg.Input(key='-INPUT-'),
      sg.FileBrowse(file_types=(("JSON Files", "*.json"), ("ALL Files", "*.*"))),
      sg.Button("Abrir"),
    ]
  ]
  window = sg.Window('Abrir arquivo', layout, resizable=True)
  while True:
    event, values = window.read(close=True)
    if event == sg.WINDOW_CLOSED:
      break
    elif event == 'Abrir':
      filename = values['-INPUT-']
      if Path(filename).is_file():
        try:
          with open(filename, encoding='utf-8') as fp:
            listObj = json.load(fp)
            print(listObj)
            return create_user_from_file(listObj)
        except Exception as e:
          result_window('Erro no processo de carregar arquivo.')



def load_file_gui_property():
  layout = [
    [
      sg.Input(key='-INPUT-'),
      sg.FileBrowse(file_types=(("JSON Files", "*.json"), ("ALL Files", "*.*"))),
      sg.Button("Abrir"),
    ]
  ]
  window = sg.Window('Abrir arquivo', layout, resizable=True)
  while True:
    event, values = window.read(close=True)
    if event == sg.WINDOW_CLOSED:
      break
    elif event == 'Abrir':
      filename = values['-INPUT-']
      if Path(filename).is_file():
        try:
          with open(filename, encoding='utf-8') as fp:
            listObj = json.load(fp)
            print(listObj)
            return create_property_from_file(listObj)
        except Exception as e:
          result_window('Erro no processo de carregar arquivo.')

def load_file_gui_insurance():
  layout = [
    [
      sg.Input(key='-INPUT-'),
      sg.FileBrowse(file_types=(("JSON Files", "*.json"), ("ALL Files", "*.*"))),
      sg.Button("Abrir"),
    ]
  ]
  window = sg.Window('Abrir arquivo', layout, resizable=True)
  while True:
    event, values = window.read(close=True)
    if event == sg.WINDOW_CLOSED:
      break
    elif event == 'Abrir':
      filename = values['-INPUT-']
      if Path(filename).is_file():
        try:
          with open(filename, encoding='utf-8') as fp:
            listObj = json.load(fp)
            print(listObj)
            return create_insurance_from_file(listObj)
        except Exception as e:
          result_window('Erro no processo de carregar arquivo.')

def load_file_gui_sales(user_list: list, property_list: list, payment_list: list)-> list:
  layout = [
    [
      sg.Input(key='-INPUT-'),
      sg.FileBrowse(file_types=(("JSON Files", "*.json"), ("ALL Files", "*.*"))),
      sg.Button("Abrir"),
    ]
  ]
  window = sg.Window('Abrir arquivo', layout, resizable=True)
  while True:
    event, values = window.read(close=True)
    if event == sg.WINDOW_CLOSED:
      break
    elif event == 'Abrir':
      filename = values['-INPUT-']
      if Path(filename).is_file():
        #try:
          with open(filename, encoding='utf-8') as fp:
            listObj = json.load(fp)
            print(listObj)
            return create_sale_from_file(listObj, user_list, property_list,  payment_list)
        #except Exception as e:
          #result_window('Erro no processo de carregar arquivo.')
# FIM Lógica de carregar arquivos