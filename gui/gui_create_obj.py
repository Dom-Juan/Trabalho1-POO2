import PySimpleGUI as sg
import sys

sys.path.append('..\\')

from classes.money.insurance import Insurance
from classes.money.payment_method_card import PaymentByCard
from classes.money.payment_method_money import PaymentByMoney

# import de classes
from classes.user.user_client import UserClient
from classes.user.user_broker import UserBroker
from classes.property.residential_apartment import ResidentialApartment
from classes.property.residential_home import ResidentialHome
from classes.property.comercial import Comercial
from classes.sales.sales import Sale
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
def create_user_from_file(list_obj) -> list:
  loaded_users_from_file: list = []
  loaded_user: object = None
  for data in list_obj:
    if data["type"] == "client":
      loaded_user = UserClient(
        str(data["name"]),
        str(data["cpf"]),
        str(data["rg"]),
        data["anniversary_date"],
        str(data["address"]),
        str(data["cep"]),
        str(data["phone"]),
        str(data["email"])
      )
      loaded_user.user_code = data["user_code"]
      loaded_user.register_date = data["register_date"]
    elif data["type"] == "broker":
      loaded_user = UserBroker(
        str(data["name"]),
        str(data["cpf"]),
        str(data["rg"]),
        data["anniversary_date"],
        str(data["address"]),
        str(data["cep"]),
        str(data["phone"]),
        str(data["email"]),
        str(data["growf"]),
        float(data["wage"]),
        str(data["pis"]),
        data["hired_date"]
      )
      loaded_user.user_code = data["user_code"]
      loaded_user.hired_date = data["hired_date"]
    else:
      print("ERROR, NULL DETECTADO!!!")
      continue
    loaded_users_from_file.append(loaded_user)
  print("> Usuários carregados com sucesso! ", loaded_users_from_file)
  return loaded_users_from_file

# Imóvel
def create_property_from_file(list_obj) -> list:
  loaded_property_from_file: list = []
  prop: object = None
  print(list_obj)
  for data in list_obj:
    prop = None
    if data["type"] == "residential_apartment":
      prop = ResidentialApartment(
        data["address"],
        data["construction_date"],
        data["total_area"],
        data["constructed_area"],
        data["num_rooms"],
        data["num_bathrooms"],
        data["num_spots_garage"],
        float(data["iptu"]),
        float(data["property_worth"]),
        float(data["property_rent"]),
        data["floor"],
        float(data["apartment_value"]),
      )
      prop.property_code = data["property_code"]
    elif data["type"] == "residential_home":
      prop = ResidentialHome(
        data["address"],
        data["construction_date"],
        data["total_area"],
        data["constructed_area"],
        data["num_rooms"],
        data["num_bathrooms"],
        data["num_spots_garage"],
        float(data["iptu"]),
        float(data["property_worth"]),
        float(data["property_rent"]),
      )
      prop.property_code = data["property_code"]
    elif data["type"] == "comercial":
      prop = Comercial(
        data["address"],
        data["construction_date"],
        data["total_area"],
        data["constructed_area"],
        data["num_rooms"],
        data["num_bathrooms"],
        data["num_spots_garage"],
        data["iptu"],
        float(data["property_worth"]),
        float(data["property_rent"]),
        float(data["federal_tax"])
      )
      prop.property_code = data["property_code"]
    else:
      print("> ERROR - TIPO NÃO IDENTIFICADO!")
    loaded_property_from_file.append(prop)
  return loaded_property_from_file


# Cria um seguro a partir de um arquivo JSON.
def create_insurance_from_file(list_obj):
  loaded_insurance_from_file: list = []
  prop: object = None
  print(list_obj)
  for data in list_obj:
    prop = Insurance(
      str(data["insurance_name"]),
      str(data["insurance_type"]),
      str(data["insurance_desc"]),
      float(data["insurance_value"]),
    )
    prop.property_code = int(data["insurance_code"])
    loaded_insurance_from_file.append(prop)
  return loaded_insurance_from_file

def create_sale_from_file(list_obj) -> list:
  loaded_users_from_file: list = []
  loaded_user: object = None
  for data in list_obj:
    if data["type"] == "client":
      loaded_user = UserClient(
        str(data["name"]),
        str(data["cpf"]),
        str(data["rg"]),
        data["anniversary_date"],
        str(data["address"]),
        str(data["cep"]),
        str(data["phone"]),
        str(data["email"])
      )
      loaded_user.set_user_code(data["user_code"])
      loaded_user.set_register_date(data["register_date"])
    elif data["type"] == "broker":
      loaded_user = UserBroker(
        str(data["name"]),
        str(data["cpf"]),
        str(data["rg"]),
        data["anniversary_date"],
        str(data["address"]),
        str(data["cep"]),
        str(data["phone"]),
        str(data["email"]),
        str(data["growf"]),
        float(data["wage"]),
        str(data["pis"]),
        data["hired_date"]
      )
      loaded_user.set_user_code(data["user_code"])
      loaded_user.set_hired_date(data["hired_date"])
    else:
      print("ERROR, NULL DETECTADO!!!")
      continue
    loaded_users_from_file.append(loaded_user)
  print("> Usuários carregados com sucesso! ", loaded_users_from_file)
  return loaded_users_from_file

def create_sale_from_file(obj_list: list, user_list: list, property_list: list,  payment_list: list)-> list:
  client_sale: object = None
  broker_sale: object = None
  property_sale: object = None
  payment_sale: object = None
  sale_list: list = []
  print(obj_list)
  i: int = 0
  while i < len(obj_list):
    print(user_list[i])
    print(property_list[i])
    print(payment_list[i])
    if user_list[i].user_code == str(obj_list[i]["client"]):
      client_sale = user_list[i]
    elif user_list[i].user_code == str(obj_list[i]["broker"]):
      broker_sale = user_list[i]
    if property_list[i].property_code == str(obj_list[i]["sale_property"]):
      property_sale = property_list[i]
    if payment_list[i].payment_code == str(obj_list[i]["payment_code"]):
      payment_sale = payment_list[i]
    sale_list.append(Sale(
      client_sale,
      broker_sale,
      property_sale,
      str(obj_list[i]["sale_date"]),
      float(obj_list[i]["total_sale_value"]),
      payment_sale
    ))
    sale_list[i].sale_code = int(obj_list[i]["sale_code"])
    i += 1
  result_window('Operação feita com sucesso')
  print(f"GUI loop, ", sale_list, type(sale_list))
  return sale_list

# Criar pela interface
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


# Criando um novo seguro.
def create_insurance() -> object:
  insurance: object = None
  layout = [
    [sg.Text('Nome seguradora', pad=(5, 5), size=(20, 1)), sg.InputText(size=(32, 1))],
    [sg.Text('Tipo', pad=(5, 5), size=(20, 1)), sg.InputText(size=(32, 1))],
    [sg.Text('Descrição', pad=(5, 5), size=(20, 1)), sg.InputText(size=(32, 1))],
    [sg.Text('Valor', pad=(5, 5), size=(20, 1)), sg.InputText(size=(32, 1))],
    [sg.Button('Criar', pad=(5, 5), size=(21, 1), button_color=('white', 'green4'))]
  ]
  window = sg.Window("Criar Seguro", layout, element_justification='c', resizable=True, margins=(5, 5))
  while True:
    event, values = window.read(close=True)
    if '' in values or None in values:
      result_window('Algum campo está vazio, tente novamente.')
      break
    if event in ["Exit", sg.WIN_CLOSED]:
      break
    if event == "Criar":
      insurance = Insurance(
        str(values[0]),
        str(values[1]),
        str(values[2]),
        float(values[3]),
      )
      result_window('Operação feita com sucesso')
      print(f"GUI loop, ", type(insurance))
      return insurance
  window.close()


# Criando método de pagamento dinheiro
def create_payment_method_money() -> object:
  payment: object = None
  layout = [
    [sg.Text('Tipo:', pad=(5, 5), size=(20, 1)), sg.InputText(size=(32, 1))],
    [sg.Text('Quantidade a ser paga:', pad=(5, 5), size=(20, 1)), sg.InputText(size=(32, 1))],
    [sg.Button('Criar', pad=(5, 5), size=(21, 1), button_color=('white', 'green4'))]
  ]
  window = sg.Window("Criar Pagamento Dinheiro", layout, element_justification='c', resizable=True, margins=(5, 5))
  while True:
    event, values = window.read(close=True)
    if '' in values or None in values:
      result_window('Algum campo está vazio, tente novamente.')
      break
    if event in ["Exit", sg.WIN_CLOSED]:
      break
    if event == "Criar":
      payment = PaymentByMoney(
        str(values[0]),
        float(values[1]),
      )
      result_window('Operação feita com sucesso')
      print(f"GUI loop, ", type(payment))
      return payment
  window.close()


# Criando método de pagamento cartão
def create_payment_method_card() -> object:
  payment: object = None
  layout = [
    [sg.Text('Tipo:', pad=(5, 5), size=(20, 1)), sg.InputText(size=(32, 1))],
    [sg.Text('Nome no cartão:', pad=(5, 5), size=(20, 1)), sg.InputText(size=(32, 1))],
    [sg.Text('Bandeira:', pad=(5, 5), size=(20, 1)), sg.InputText(size=(32, 1))],
    [sg.Text('Número no cartão:', pad=(5, 5), size=(20, 1)), sg.InputText(size=(32, 1))],
    [sg.Button('Criar', pad=(5, 5), size=(21, 1), button_color=('white', 'green4'))]
  ]
  window = sg.Window("Criar Pagamento Cartão", layout, element_justification='c', resizable=True, margins=(5, 5))
  while True:
    event, values = window.read(close=True)
    if '' in values or None in values:
      result_window('Algum campo está vazio, tente novamente.')
      break
    if event in ["Exit", sg.WIN_CLOSED]:
      break
    if event == "Criar":
      payment = PaymentByCard(
        str(values[0]),
        str(values[1]),
        str(values[2]),
        str(values[3]),
      )
      result_window('Operação feita com sucesso')
      print(f"GUI loop, ", type(payment), values)
      return payment
  window.close()

def create_sale(user_list, property_list, payment_list) -> object:
  sale: object = None

  client_dict = {}
  broker_dict = {}
  property_dict = {}
  payment_dict = {}

  for i in user_list:
    if isinstance(i, UserClient):
      client_dict[i.name] = i
    else:
      broker_dict[i.name] = i

  for i in property_list:
    property_dict[i.address] = i
  for i in payment_list:
    payment_dict[i.payment_code] = i

  layout = [
    [sg.Text('Cliente:', pad=(5, 5), size=(20, 1)), sg.Combo(list(client_dict), size=(48, 1))],
    [sg.Text('Corretor:', pad=(5, 5), size=(20, 1)), sg.Combo(list(broker_dict), size=(48, 1))],
    [sg.Text('Imóvel:', pad=(5, 5), size=(20, 1)), sg.Combo(list(property_dict), size=(48, 1))],
    [sg.Text('Data da Venda:', pad=(5, 5), size=(20, 1)), sg.InputText(size=(48, 1))],
    [sg.Text('Valor da Venda:', pad=(5, 5), size=(20, 1)), sg.InputText(size=(48, 1))],
    [sg.Text('Tipo de Pagamento:', pad=(5, 5), size=(20, 1)), sg.Combo(list(payment_dict), size=(48, 1))],

    [sg.Button('Criar', pad=(5, 5), size=(21, 1), button_color=('white', 'green4'))]
  ]
  window = sg.Window("Criar Venda", layout, element_justification='c', resizable=True, margins=(5, 5))
  while True:
    event, values = window.read(close=True)
    if '' in values or None in values:
      result_window('Algum campo está vazio, tente novamente.')
      break
    if event in ["Exit", sg.WIN_CLOSED]:
      break
    if event == "Criar":
      print(values)
      client_sale: object = None
      broker_sale: object = None
      property_sale: object = None
      payment_sale: object = None
      for client in user_list:
        if client.name == str(values[0]):
          client_sale = client
        elif client.name == str(values[1]):
          broker_sale = client
      for property in property_list:
        if property.name == str(values[2]):
          property_sale = property
      for payment in payment_list:
        if payment.payment_type == str(values[3]):
          payment_sale = payment
      sale = Sale(
        client_sale,
        broker_sale,
        property_sale,
        str(values[3]),
        float(values[4]),
        payment_sale
      )
      result_window('Operação feita com sucesso')
      print(f"GUI loop, ", type(sale))
      return sale
  window.close()