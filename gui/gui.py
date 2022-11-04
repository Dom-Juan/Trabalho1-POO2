import PySimpleGUI as sg
import sys
import json

# import de classes
sys.path.append('../')
from classes.user.user_client import UserClient
from classes.user.user_broker import UserBroker
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
    event, values = window.read()
    if event in ["Exit", sg.WIN_CLOSED, "Ok"]:
      break
  window.close()


# Janela principal.
def main_window(name):
  sg.set_options(font=("Cascadia Code", 12))
  sg.theme('DarkAmber')
  col_create = [
    [
      sg.Text('Registar dados: ', size=(20, 2)),
      sg.Button('Criar Cliente', size=(25, 2)),
      sg.Button('Criar Corretor', size=(25, 2)),
      sg.Button('Criar Apartamento', size=(25, 2)),
      sg.Button('Criar Casa', size=(25, 2)),
      sg.Button('Criar Comercio', size=(25, 2)),
    ],
  ]
  col_show = [
    [
      sg.Text('Mostrar dados: ', size=(20, 1)),
      sg.Button('Mostrar todos Clientes', size=(25, 2)),
      sg.Button('Mostar todos Corretores', size=(25, 2)),
      sg.Button('Mostar todos Imóveis', size=(25, 2), key='-ALLPROPERTY-'),
      sg.Button('Mostar todas as Casas', size=(25, 2), key='-ALLPROPERTYHOME-'),
      sg.Button('Mostar todos os Apartamentos', size=(25, 2), key='-ALLPROPERTYAPARTMENT-'),
      sg.Button('Mostar todos os Comércios', size=(25, 2), key='-ALLPROPERTYCOMERCIAL-'),
    ]
  ]
  col_load = [
    [
      sg.Text('Carregar dados: ', size=(20, 2)),
      sg.Button('Carregar arquivo usuários', size=(25, 2)),
      sg.Button('Carregar arquivo imoveis', size=(25, 2)),
    ]
  ]
  col_save = [
    [
      sg.Text('Salvar dados: ', size=(20, 2)),
      sg.Button('Salvar arquivo usuários', size=(25, 2)),
      sg.Button('Salvar arquivo imóveis', size=(25, 2), key='-SAVEALLPROPERTY-')
    ]
  ]
  layout = [
    [
      sg.Column(col_create),
    ],
    [
      sg.Column(col_show),
    ],
    [
      sg.Column(col_load)
    ],
    [
      sg.Column(col_save),
    ],
    [sg.Button('Sair', size=(15, 1), button_color=('white', 'firebrick3'))]
  ]
  layout2 = []  # layout da janela
  # Configurações da página.
  window = sg.Window(name, layout, size=(1380, 720), resizable=True, margins=(5, 5), finalize=True)
  # Array de objetos instanciados.
  user_list: list = list()
  property_list: list = list()
  # Objetos instanciados com Null para receberem os ponteiros depois.
  u: object = None
  p: object = None
  while True:
    event, values = window.read()
    layout2.append([sg.Text('Resultado'), values])
    if event in [sg.WIN_CLOSED, 'Sair']:
      break
    # Lógica de criação dos objetos.
    if event == "Criar Cliente":
      u = create_client()
      print(f"Main loop, ", u)
      user_list.append(u)
    if event == "Criar Corretor":
      u = create_broker()
      print(f"Main loop, ", u)
      user_list.append(u)
    if event == "Criar Apartamento":
      ap = create_apartment()
      print(f"Main loop, ", ap)
      property_list.append(ap)
    # Lógica de mostrar info dos objetos.
    if event == "Mostrar todos Clientes":
      print_info(UserClient, user_list)
    if event == "Mostar todos Corretores":
      print_info(UserBroker, user_list)
    if event == "Carregar arquivo usuários":
      new_user_list: list = load_file_gui_users()
      if new_user_list != None:
        for u in new_user_list[:]:
          user_list.append(u)
        result_window('Arquivo carregado com sucesso!')
    if event == 'Carregar arquivo imoveis':
      new_property_list: list = load_file_gui_property()
      if new_property_list != None:
        for p in new_property_list[:]:
          property_list.append(p)
        result_window('Arquivo carregado com sucesso!')
    if event == "Salvar arquivo usuários":
      for u in user_list:
        u.save_json_file()
  window.close()


# Função helper para printa as info dos obj.
def print_info(obj_type, obj_array):
  for obj in obj_array[:]:
    if type(obj) == obj_type:
      obj.print_obj()
  pass


# Lógica de criação de objetos
# Imóvel
def create_property_from_file(listObj) -> list:
  loaded_property_from_file: list = []
  loaded_property: object = None
  for data in listObj:
    data = 1
  return loaded_property_from_file


# Cliente
def create_user_from_file(listObj) -> list:
  loaded_users_from_file: list = []
  loaded_user: object = None
  for data in listObj:
    if (data['type'] == 'client'):
      loaded_user = UserClient(
        data['name'],
        data['cpf'],
        data['rg'],
        data['anniversary_date'],
        data['address'],
        data['cep'],
        data['phone'],
        data['email']
      )
      loaded_user.set_user_code(data['user_code'])
      loaded_user.set_register_date(data['register_date'])
    elif (data['type'] == 'broker'):
      loaded_user = UserBroker(
        data['name'],
        data['cpf'],
        data['rg'],
        data['anniversary_date'],
        data['address'],
        data['cep'],
        data['phone'],
        data['email'],
        data['growf'],
        data['wage'],
        data['pis'],
        data['hired_date']
      )
      loaded_user.set_user_code(data['user_code'])
      loaded_user.set_hired_date(data['hired_date'])
    else:
      print("ERROR, NULL DETECTADO!!!")
      continue
    loaded_users_from_file.append(loaded_user)
  print("> Usuários carregados com sucesso! ", loaded_users_from_file)
  return loaded_users_from_file

# Criar um cliente
def create_client() -> object:
  user: object = None
  layout = [
    [sg.Text('Nome completo', pad=(5, 5), size=(20, 1)), sg.InputText(size=(32, 1))],
    [sg.Text('CPF', pad=(5, 5), size=(20, 1)), sg.InputText(size=(32, 1))],
    [sg.Text('RG', pad=(5, 5), size=(20, 1)), sg.InputText(size=(32, 1))],
    [sg.Text('Data de nascimento', pad=(5, 5), size=(20, 1)), sg.InputText(size=(32, 1))],
    [sg.Text('Endereço', pad=(5, 5), size=(20, 1)), sg.InputText(size=(32, 1))],
    [sg.Text('CEP', pad=(5, 5), size=(20, 1)), sg.InputText(size=(32, 1))],
    [sg.Text('Telefone', pad=(5, 5), size=(20, 1)), sg.InputText(size=(32, 1))],
    [sg.Text('Email', pad=(5, 5), size=(20, 1)), sg.InputText(size=(32, 1))],
    [sg.Button('Criar', pad=(5, 5), size=(20, 1), button_color=('white', 'green4'))]
  ]
  window = sg.Window("Criar cliente", layout, element_justification='c', resizable=True, margins=(5, 5))
  while True:
    event, values = window.read()
    if event in ["Exit", sg.WIN_CLOSED]:
      break
    if event == "Criar":
      user = UserClient(
        values[0],
        values[1],
        values[2],
        values[3],
        values[4],
        values[5],
        values[6],
        values[7],
      )
      result_window('Operação feita com sucesso')
      print(f"GUI loop, ", type(user))
      return user
      window.close()
  window.close()


# Criar um corretor
def create_broker() -> object:
  user: object = None
  layout = [
    [sg.Text('Nome completo', pad=(5, 5), size=(20, 1)), sg.InputText(size=(32, 1))],
    [sg.Text('CPF', pad=(5, 5), size=(20, 1)), sg.InputText(size=(32, 1))],
    [sg.Text('RG', pad=(5, 5), size=(20, 1)), sg.InputText(size=(32, 1))],
    [sg.Text('Data de nascimento', pad=(5, 5), size=(20, 1)), sg.InputText(size=(32, 1))],
    [sg.Text('Endereço', pad=(5, 5), size=(20, 1)), sg.InputText(size=(32, 1))],
    [sg.Text('CEP', pad=(5, 5), size=(20, 1)), sg.InputText(size=(32, 1))],
    [sg.Text('Telefone', pad=(5, 5), size=(20, 1)), sg.InputText(size=(32, 1))],
    [sg.Text('Email', pad=(5, 5), size=(20, 1)), sg.InputText(size=(32, 1))],
    [sg.Text('Creci', pad=(5, 5), size=(20, 1)), sg.InputText(size=(32, 1))],
    [sg.Text('Salário', pad=(5, 5), size=(20, 1)), sg.InputText(size=(32, 1))],
    [sg.Text('pis', pad=(5, 5), size=(20, 1)), sg.InputText(size=(32, 1))],
    [sg.Text('data de adimissão', pad=(5, 5), size=(20, 1)), sg.InputText(size=(32, 1))],
    [sg.Button('Criar', pad=(5, 5), size=(20, 1), button_color=('white', 'green4'))]
  ]
  window = sg.Window("Criar corretor", layout, element_justification='c', resizable=True, margins=(5, 5))
  while True:
    event, values = window.read()
    if event in ["Exit", sg.WIN_CLOSED]:
      break
    if event == "Criar":
      print(values)
      user = UserBroker(
        values[0],
        values[1],
        values[2],
        values[3],
        values[4],
        values[5],
        values[6],
        values[7],
        values[8],
        values[9],
        values[10],
        values[11],
      )
      result_window('Operação feita com sucesso')
      print(f"GUI loop, ", type(user))
      return user
      window.close()
  window.close()


# Propriedades
# Cirando um apartamento
def create_apartment() -> object:
  user: object = None
  layout = [
    [sg.Text('Endereço', pad=(5, 5), size=(20, 1)), sg.InputText(size=(32, 1))],
    [sg.Text('Data construção', pad=(5, 5), size=(20, 1)), sg.InputText(size=(32, 1))],
    [sg.Text('Area total', pad=(5, 5), size=(20, 1)), sg.InputText(size=(32, 1))],
    [sg.Text('Area construida', pad=(5, 5), size=(20, 1)), sg.InputText(size=(32, 1))],
    [sg.Text('Quantidade Dorm.', pad=(5, 5), size=(20, 1)), sg.InputText(size=(32, 1))],
    [sg.Text('Quantidade Banheiros', pad=(5, 5), size=(20, 1)), sg.InputText(size=(32, 1))],
    [sg.Text('Vagas na garagem', pad=(5, 5), size=(20, 1)), sg.InputText(size=(32, 1))],
    [sg.Text('IPTU', pad=(5, 5), size=(20, 1)), sg.InputText(size=(32, 1))],
    [sg.Text('Valor da venda', pad=(5, 5), size=(20, 1)), sg.InputText(size=(32, 1))],
    [sg.Text('Valor do aluguel', pad=(5, 5), size=(20, 1)), sg.InputText(size=(32, 1))],
    [sg.Text('Andar do AP', pad=(5, 5), size=(20, 1)), sg.InputText(size=(32, 1))],
    [sg.Text('Valor do condomínio', pad=(5, 5), size=(20, 1)), sg.InputText(size=(32, 1))],
    [sg.Button('Criar', pad=(5, 5), size=(20, 1), button_color=('white', 'green4'))]
  ]
  window = sg.Window("Criar cliente", layout, element_justification='c', resizable=True, margins=(5, 5))
  while True:
    event, values = window.read()
    if event in ["Exit", sg.WIN_CLOSED]:
      break
    if event == "Criar":
      user = UserClient(
        values[0],
        values[1],
        values[2],
        values[3],
        values[4],
        values[5],
        values[6],
        values[7],
        values[8],
        values[9],
        values[10],
        values[11],
        values[12]
      )
      result_window('Operação feita com sucesso')
      print(f"GUI loop, ", type(user))
      return user
      window.close()
  window.close()

# FIM Lógica de criação de objetos




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
    event, values = window.read()
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
    event, values = window.read()
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
# FIM Lógica de carregar arquivos

# Lógica de salvar dados em JSON
def save_to_file(list) -> True:
  todo = "TODO"
  print(todo)
  return True


# FIM Lógica de salvar dados em JSON
