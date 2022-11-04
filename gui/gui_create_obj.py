import PySimpleGUI as sg
import sys

# import de classes
sys.path.append('../')
from classes.user.user_client import UserClient
from classes.user.user_broker import UserBroker
from classes.property.residential_apartment import ResidentialApartment
from classes.property.residential_home import ResidentialHome
from classes.property.comercial import Comercial
from helpers.helper import check_if_all_none, check_if_all_empty

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

# Lógica de criação de objetos
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

# Imóvel
def create_property_from_file(listObj) -> list:
  loaded_property_from_file: list = []
  loaded_property: object = None
  for data in listObj:
    data = 1
  return loaded_property_from_file

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
  window = sg.Window("Criar Cliente", layout, element_justification='c', resizable=True, margins=(5, 5))
  while True:
    event, values = window.read(close=True)
    if '' in values or None in values:
      result_window('Algum campo está vazio, tente novamente.')
      break
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
        values[7]
      )
      result_window('Operação feita com sucesso')
      print(f"GUI loop, ", type(user))
      return user
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
  window = sg.Window("Criar Corretor", layout, element_justification='c', resizable=True, margins=(5, 5))
  while True:
    event, values = window.read(close=True)
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


# Propriedades
# Cirando um apartamento
def create_apartment() -> object:
  ap: object = None
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
  window = sg.Window("Criar Apartamento", layout, element_justification='c', resizable=True, margins=(5, 5))
  while True:
    event, values = window.read(close=True)
    if event in ["Exit", sg.WIN_CLOSED]:
      break
    if event == "Criar":
      ap = ResidentialApartment(
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
      print(f"GUI loop, ", type(ap))
      return ap
  window.close()

# Cria uma Casa
def create_house() -> object:
  h: object = None
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
    [sg.Button('Criar', pad=(5, 5), size=(20, 1), button_color=('white', 'green4'))]
  ]
  window = sg.Window("Criar uma Casa", layout, element_justification='c', resizable=True, margins=(5, 5))
  while True:
    event, values = window.read(close=True)
    if event in ["Exit", sg.WIN_CLOSED]:
      break
    if event == "Criar":
      home = ResidentialHome(
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
      )
      result_window('Operação feita com sucesso')
      print(f"GUI loop, ", type(h))
      return h
  window.close()

# Cria uma Casa
def create_comercial() -> object:
  c: object = None
  layout = [
    [sg.Text('Endereço', pad=(5, 5), size=(21, 1)), sg.InputText(size=(32, 1))],
    [sg.Text('Data construção', pad=(5, 5), size=(21, 1)), sg.InputText(size=(32, 1))],
    [sg.Text('Area total', pad=(5, 5), size=(21, 1)), sg.InputText(size=(32, 1))],
    [sg.Text('Area construida', pad=(5, 5), size=(21, 1)), sg.InputText(size=(32, 1))],
    [sg.Text('Quantidade Dorm.', pad=(5, 5), size=(21, 1)), sg.InputText(size=(32, 1))],
    [sg.Text('Quantidade Banheiros', pad=(5, 5), size=(21, 1)), sg.InputText(size=(32, 1))],
    [sg.Text('Vagas na garagem', pad=(5, 5), size=(21, 1)), sg.InputText(size=(32, 1))],
    [sg.Text('IPTU', pad=(5, 5), size=(21, 1)), sg.InputText(size=(32, 1))],
    [sg.Text('Valor da venda', pad=(5, 5), size=(21, 1)), sg.InputText(size=(32, 1))],
    [sg.Text('Valor do aluguel', pad=(5, 5), size=(21, 1)), sg.InputText(size=(32, 1))],
    [sg.Text('Taxa imposto federal:', pad=(5, 5), size=(21, 1)), sg.InputText(size=(32, 1))],
    [sg.Button('Criar', pad=(5, 5), size=(21, 1), button_color=('white', 'green4'))]
  ]
  window = sg.Window("Criar um Comércio", layout, element_justification='c', resizable=True, margins=(5, 5))
  while True:
    event, values = window.read(close=True)
    if event in ["Exit", sg.WIN_CLOSED]:
      break
    if event == "Criar":
      c = Comercial(
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
        values[10]
      )
      result_window('Operação feita com sucesso')
      print(f"GUI loop, ", type(c))
      return c
  window.close()

# FIM Lógica de criação de objetos