import PySimpleGUI as sg
import sys

from classes.money.insurance import Insurance
from classes.property.comercial import Comercial
from classes.property.residential_home import ResidentialHome

# import de classes
sys.path.append('../')
from classes.user.user_client import UserClient
from classes.user.user_broker import UserBroker
from classes.property.residential_apartment import ResidentialApartment


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


# Mostrar Objetos
# Função helper para printa as info dos obj.
def print_info(obj_type, obj_array):
  for obj in obj_array[:]:
    if type(obj) == obj_type:
      obj.print_obj()
  pass


# Mostrar Usuários
def show_users(user_list: list, type: str) -> None:
  print(user_list)
  Col = []
  Col.append([sg.Text('Mostrando informações')])
  for user in user_list:
    if user is not None:
      if isinstance(user, UserClient):
        # layout da página.
        Col.append([sg.HSeparator()])
        Col.append([
          sg.Text('ID:', pad=(5, 5), size=(20, 1)),  # Label
          sg.Text(str(user.get_user_code()), pad=(5, 5), size=(20, 1))  # Valor do obj.
        ])
        Col.append(
          [
            sg.Text('Nome: ', pad=(5, 5), size=(20, 1)),
            sg.Text(str(user.get_name()), pad=(5, 5), size=(20, 1))
          ]
        )
        Col.append(
          [
            sg.Text('CPF:', pad=(5, 5), size=(20, 1)),
            sg.Text(str(user.get_cpf()), pad=(5, 5), size=(20, 1))
          ]
        )
        Col.append(
          [
            sg.Text('RG:', pad=(5, 5), size=(20, 1)),
            sg.Text(str(user.get_rg()), pad=(5, 5), size=(20, 1))
          ]
        )
        Col.append(
          [
            sg.Text('Ano de nascimento:', pad=(5, 5), size=(20, 1)),
            sg.Text(str(user.get_anniversary_date()), pad=(5, 5), size=(20, 1))
          ]
        )
        Col.append(
          [
            sg.Text('Endereço:', pad=(5, 5), size=(20, 1)),
            sg.Text(str(user.get_address()), pad=(5, 5), size=(20, 1))
          ]
        )
        Col.append(
          [
            sg.Text('CEP:', pad=(5, 5), size=(20, 1)),
            sg.Text(str(user.get_cep()), pad=(5, 5), size=(20, 1))
          ]
        )
        Col.append(
          [
            sg.Text('Telefone:', pad=(5, 5), size=(20, 1)),
            sg.Text(str(user.get_phone()), pad=(5, 5), size=(20, 1))
          ]
        )
        Col.append(
          [
            sg.Text('Email:', pad=(5, 5), size=(20, 1)),
            sg.Text(str(user.get_email()), pad=(5, 5), size=(20, 1))
          ]
        )
        if type == "clientes":  # Verificação para interface.
          if isinstance(user, UserClient):  # verificando o tipo de obj.
            Col.append(
              [
                sg.Text('Data de registro:', pad=(5, 5), size=(20, 1)),
                sg.Text(str(user.get_register_date()), pad=(5, 5), size=(20, 1))
              ]
            )
        if type == "corretores":  # Verificação para interface.
          if isinstance(user, UserBroker):  # verificando o tipo de obj.
            Col.append(
              [
                sg.Text('Crescimento:', pad=(5, 5), size=(20, 1)),
                sg.Text(str(user.get_growf()), pad=(5, 5), size=(20, 1))
              ]
            )
            Col.append(
              [
                sg.Text('Salário:', pad=(5, 5), size=(20, 1)),
                sg.Text(str(user.get_wage()), pad=(5, 5), size=(20, 1))
              ]
            )
            Col.append(
              [
                sg.Text('PIS:', pad=(5, 5), size=(20, 1)),
                sg.Text(str(user.get_pis()), pad=(5, 5), size=(20, 1))
              ]
            )
            Col.append(
              [
                sg.Text('Data de admissão:', pad=(5, 5), size=(20, 1)),
                sg.Text(str(user.get_hired_date()), pad=(5, 5), size=(20, 1))
              ]
            )
      Col.append([sg.HSeparator()])
    layout = []
    layout.append([sg.Column(Col, element_justification='c', scrollable=True, vertical_scroll_only=True)])
    layout.append([sg.Button('Sair', size=(15, 1), button_color=('white', 'firebrick3'))])
    window = sg.Window("Mostrando Todos Clientes", layout, element_justification='c', resizable=True, finalize=True,
                       modal=True)
    window.TKroot.minsize(320, 240)
    while True:
      event, values = window.read(close=True)
      if event in ["Exit", sg.WIN_CLOSED, "Sair"]:
        break
    window.close()


# Mostrar Apartamentos
def show_property(property_list: list, type: str) -> None:
  layout = []
  Col = []
  for property in property_list:
    if property is not None:
      # layout da página.
      Col.append([sg.HSeparator()])
      Col.append([
        sg.Text('ID:', pad=(5, 5), size=(20, 1)),  # Label
        sg.Text(str(property.property_code), pad=(5, 5), size=(20, 1))  # Valor do obj.
      ])
      Col.append(
        [
          sg.Text('Endereço: ', pad=(5, 5), size=(20, 1)),
          sg.Text(str(property.address), pad=(5, 5), size=(20, 1))
        ]
      )
      Col.append(
        [
          sg.Text('Data de construção:', pad=(5, 5), size=(20, 1)),
          sg.Text(str(property.construction_date), pad=(5, 5), size=(20, 1))
        ]
      )
      Col.append(
        [
          sg.Text('Área total:', pad=(5, 5), size=(20, 1)),
          sg.Text(str(property.total_area), pad=(5, 5), size=(20, 1))
        ]
      )
      Col.append(
        [
          sg.Text('Área de construção:', pad=(5, 5), size=(20, 1)),
          sg.Text(str(property.constructed_area), pad=(5, 5), size=(20, 1))
        ]
      )
      Col.append(
        [
          sg.Text('Num. de quartos:', pad=(5, 5), size=(20, 1)),
          sg.Text(str(property.num_rooms), pad=(5, 5), size=(20, 1))
        ]
      )
      Col.append(
        [
          sg.Text('Num. de banheiros:', pad=(5, 5), size=(20, 1)),
          sg.Text(str(property.num_bathrooms), pad=(5, 5), size=(20, 1))
        ]
      )
      Col.append(
        [
          sg.Text('Num. de vagas:', pad=(5, 5), size=(20, 1)),
          sg.Text(str(property.num_spots_garage), pad=(5, 5), size=(20, 1))
        ]
      )
      Col.append(
        [
          sg.Text('IPTU:', pad=(5, 5), size=(20, 1)),
          sg.Text(str(property.iptu), pad=(5, 5), size=(20, 1))
        ]
      )
      Col.append(
        [
          sg.Text('Valor propriedade:', pad=(5, 5), size=(20, 1)),
          sg.Text(str(property.property_worth), pad=(5, 5), size=(20, 1))
        ]
      )
      Col.append(
        [
          sg.Text('Valor de aluguel:', pad=(5, 5), size=(20, 1)),
          sg.Text(str(property.property_rent), pad=(5, 5), size=(20, 1))
        ]
      )
      Col.append([sg.HSeparator()])
      if type == "ap":
        if isinstance(property, ResidentialApartment):
          Col.append(
            [
              sg.Text('Andar do ap:', pad=(5, 5), size=(20, 1)),
              sg.Text(str(property.apartment_value), pad=(5, 5), size=(20, 1))
            ]
          )
          Col.append(
            [
              sg.Text('Valor do ap:', pad=(5, 5), size=(20, 1)),
              sg.Text(str(property.apartment_value), pad=(5, 5), size=(20, 1))
            ]
          )
      elif type == "c":
        if isinstance(property, Comercial):
          Col.append(
            [
              sg.Text('Imposto federal:', pad=(5, 5), size=(20, 1)),
              sg.Text(str(property.federal_tax), pad=(5, 5), size=(20, 1))
            ]
          )
  layout.append([sg.Text('Mostrando informações', pad=(5, 5), size=(25, 1))])
  layout.append([sg.Column(Col, element_justification='c', scrollable=True, vertical_scroll_only=True)])
  layout.append([sg.Button('Sair', size=(15, 1), button_color=('white', 'firebrick3'))])
  window = sg.Window("Mostrando Todos Apartamentos", layout, element_justification='c', resizable=True, finalize=True,
                     modal=True)
  window.TKroot.minsize(320, 240)
  while True:
    event, values = window.read(close=True)
    if event in ["Exit", sg.WIN_CLOSED, "Sair"]:
      break
  window.close()


# Mostra todas propriedades.
def show_all_property(property_list):
  layout = []
  Col = []
  if None in property_list:
    result_window('Erro, existe NULL no vetor.')
    return False
  for prop in property_list:
    if prop is not None:
      # layout da página.
      Col.append([sg.HSeparator()])
      Col.append([
        sg.Text('ID:', pad=(5, 5), size=(20, 1)),  # Label
        sg.Text(str(prop.property_code), pad=(5, 5), size=(20, 1))  # Valor do obj.
      ])
      Col.append(
        [
          sg.Text('Endereço: ', pad=(5, 5), size=(20, 1)),
          sg.Text(str(prop.address), pad=(5, 5), size=(20, 1))
        ]
      )
      Col.append(
        [
          sg.Text('Data de construção:', pad=(5, 5), size=(20, 1)),
          sg.Text(str(prop.construction_date), pad=(5, 5), size=(20, 1))
        ]
      )
      Col.append(
        [
          sg.Text('Área total:', pad=(5, 5), size=(20, 1)),
          sg.Text(str(prop.total_area), pad=(5, 5), size=(20, 1))
        ]
      )
      Col.append(
        [
          sg.Text('Área de construção:', pad=(5, 5), size=(20, 1)),
          sg.Text(str(prop.constructed_area), pad=(5, 5), size=(20, 1))
        ]
      )
      Col.append(
        [
          sg.Text('Num. de quartos:', pad=(5, 5), size=(20, 1)),
          sg.Text(str(prop.num_rooms), pad=(5, 5), size=(20, 1))
        ]
      )
      Col.append(
        [
          sg.Text('Num. de banheiros:', pad=(5, 5), size=(20, 1)),
          sg.Text(str(prop.num_bathrooms), pad=(5, 5), size=(20, 1))
        ]
      )
      Col.append(
        [
          sg.Text('Num. de vagas:', pad=(5, 5), size=(20, 1)),
          sg.Text(str(prop.num_spots_garage), pad=(5, 5), size=(20, 1))
        ]
      )
      Col.append(
        [
          sg.Text('IPTU:', pad=(5, 5), size=(20, 1)),
          sg.Text(str(prop.iptu), pad=(5, 5), size=(20, 1))
        ]
      )
      Col.append(
        [
          sg.Text('Valor propriedade:', pad=(5, 5), size=(20, 1)),
          sg.Text(str(prop.property_worth), pad=(5, 5), size=(20, 1))
        ]
      )
      Col.append(
        [
          sg.Text('Valor de aluguel:', pad=(5, 5), size=(20, 1)),
          sg.Text(str(prop.property_rent), pad=(5, 5), size=(20, 1))
        ]
      )
      Col.append([sg.HSeparator()])
      if isinstance(prop, ResidentialApartment):
        Col.append(
          [
            sg.Text('Andar do ap:', pad=(5, 5), size=(20, 1)),
            sg.Text(str(prop.apartment_value), pad=(5, 5), size=(20, 1))
          ]
        )
        Col.append(
          [
            sg.Text('Valor do ap:', pad=(5, 5), size=(20, 1)),
            sg.Text(str(prop.apartment_value), pad=(5, 5), size=(20, 1))
          ]
        )
      if isinstance(prop, Comercial):
        Col.append(
          [
            sg.Text('Imposto federal:', pad=(5, 5), size=(20, 1)),
            sg.Text(str(prop.federal_tax), pad=(5, 5), size=(20, 1))
          ]
        )
  layout.append([sg.Text('Mostrando informações', pad=(5, 5), size=(25, 1))])
  layout.append([sg.Column(Col, element_justification='c', scrollable=True, vertical_scroll_only=True)])
  layout.append([sg.Button('Sair', size=(15, 1), button_color=('white', 'firebrick3'))])
  window = sg.Window("Mostrando Todos Apartamentos", layout, element_justification='c', resizable=True, finalize=True,
                     modal=True)
  window.TKroot.minsize(320, 240)
  while True:
    event, values = window.read(close=True)
    if event in ["Exit", sg.WIN_CLOSED, "Sair"]:
      break
  window.close()


# Mostra apenas apartamentos.
def show_ap_property(property_list):
  layout = []
  Col = []
  if None in property_list:
    result_window('Erro, existe NULL no vetor.')
    return False
  for prop in property_list:
    if prop is not None:
      if isinstance(prop, ResidentialApartment):
        # layout da página.
        Col.append([sg.HSeparator()])
        Col.append([
          sg.Text('ID:', pad=(5, 5), size=(20, 1)),  # Label
          sg.Text(str(prop.property_code), pad=(5, 5), size=(20, 1))  # Valor do obj.
        ])
        Col.append(
          [
            sg.Text('Endereço: ', pad=(5, 5), size=(20, 1)),
            sg.Text(str(prop.address), pad=(5, 5), size=(20, 1))
          ]
        )
        Col.append(
          [
            sg.Text('Data de construção:', pad=(5, 5), size=(20, 1)),
            sg.Text(str(prop.construction_date), pad=(5, 5), size=(20, 1))
          ]
        )
        Col.append(
          [
            sg.Text('Área total:', pad=(5, 5), size=(20, 1)),
            sg.Text(str(prop.total_area), pad=(5, 5), size=(20, 1))
          ]
        )
        Col.append(
          [
            sg.Text('Área de construção:', pad=(5, 5), size=(20, 1)),
            sg.Text(str(prop.constructed_area), pad=(5, 5), size=(20, 1))
          ]
        )
        Col.append(
          [
            sg.Text('Num. de quartos:', pad=(5, 5), size=(20, 1)),
            sg.Text(str(prop.num_rooms), pad=(5, 5), size=(20, 1))
          ]
        )
        Col.append(
          [
            sg.Text('Num. de banheiros:', pad=(5, 5), size=(20, 1)),
            sg.Text(str(prop.num_bathrooms), pad=(5, 5), size=(20, 1))
          ]
        )
        Col.append(
          [
            sg.Text('Num. de vagas:', pad=(5, 5), size=(20, 1)),
            sg.Text(str(prop.num_spots_garage), pad=(5, 5), size=(20, 1))
          ]
        )
        Col.append(
          [
            sg.Text('IPTU:', pad=(5, 5), size=(20, 1)),
            sg.Text(str(prop.iptu), pad=(5, 5), size=(20, 1))
          ]
        )
        Col.append(
          [
            sg.Text('Valor propriedade:', pad=(5, 5), size=(20, 1)),
            sg.Text(str(prop.property_worth), pad=(5, 5), size=(20, 1))
          ]
        )
        Col.append(
          [
            sg.Text('Valor de aluguel:', pad=(5, 5), size=(20, 1)),
            sg.Text(str(prop.property_rent), pad=(5, 5), size=(20, 1))
          ]
        )
        Col.append([sg.HSeparator()])
        Col.append(
          [
            sg.Text('Andar do ap:', pad=(5, 5), size=(20, 1)),
            sg.Text(str(prop.apartment_value), pad=(5, 5), size=(20, 1))
          ]
        )
        Col.append(
          [
            sg.Text('Valor do ap:', pad=(5, 5), size=(20, 1)),
            sg.Text(str(prop.apartment_value), pad=(5, 5), size=(20, 1))
          ]
        )
  layout.append([sg.Text('Mostrando informações', pad=(5, 5), size=(25, 1))])
  layout.append([sg.Column(Col, element_justification='c', scrollable=True, vertical_scroll_only=True)])
  layout.append([sg.Button('Sair', size=(15, 1), button_color=('white', 'firebrick3'))])
  window = sg.Window("Mostrando Todos Apartamentos", layout, element_justification='c', resizable=True, finalize=True,
                     modal=True)
  window.TKroot.minsize(320, 240)
  while True:
    event, values = window.read(close=True)
    if event in ["Exit", sg.WIN_CLOSED, "Sair"]:
      break
  window.close()


# Mostra todos imóveis comerciais
def show_comercial_property(property_list):
  layout = []
  Col = []
  if None in property_list:
    result_window('Erro, existe NULL no vetor.')
    return False
  for prop in property_list:
    if prop is not None:
      print(isinstance(prop, Comercial), type(prop))
      if isinstance(prop, Comercial):
        print(prop)
        # layout da página.
        Col.append([sg.HSeparator()])
        Col.append([
          sg.Text('ID:', pad=(5, 5), size=(20, 1)),  # Label
          sg.Text(str(prop.property_code), pad=(5, 5), size=(20, 1))  # Valor do obj.
        ])
        Col.append(
          [
            sg.Text('Endereço: ', pad=(5, 5), size=(20, 1)),
            sg.Text(str(prop.address), pad=(5, 5), size=(20, 1))
          ]
        )
        Col.append(
          [
            sg.Text('Data de construção:', pad=(5, 5), size=(20, 1)),
            sg.Text(str(prop.construction_date), pad=(5, 5), size=(20, 1))
          ]
        )
        Col.append(
          [
            sg.Text('Área total:', pad=(5, 5), size=(20, 1)),
            sg.Text(str(prop.total_area), pad=(5, 5), size=(20, 1))
          ]
        )
        Col.append(
          [
            sg.Text('Área de construção:', pad=(5, 5), size=(20, 1)),
            sg.Text(str(prop.constructed_area), pad=(5, 5), size=(20, 1))
          ]
        )
        Col.append(
          [
            sg.Text('Num. de quartos:', pad=(5, 5), size=(20, 1)),
            sg.Text(str(prop.num_rooms), pad=(5, 5), size=(20, 1))
          ]
        )
        Col.append(
          [
            sg.Text('Num. de banheiros:', pad=(5, 5), size=(20, 1)),
            sg.Text(str(prop.num_bathrooms), pad=(5, 5), size=(20, 1))
          ]
        )
        Col.append(
          [
            sg.Text('Num. de vagas:', pad=(5, 5), size=(20, 1)),
            sg.Text(str(prop.num_spots_garage), pad=(5, 5), size=(20, 1))
          ]
        )
        Col.append(
          [
            sg.Text('IPTU:', pad=(5, 5), size=(20, 1)),
            sg.Text(str(prop.iptu), pad=(5, 5), size=(20, 1))
          ]
        )
        Col.append(
          [
            sg.Text('Valor propriedade:', pad=(5, 5), size=(20, 1)),
            sg.Text(str(prop.property_worth), pad=(5, 5), size=(20, 1))
          ]
        )
        Col.append(
          [
            sg.Text('Valor de aluguel:', pad=(5, 5), size=(20, 1)),
            sg.Text(str(prop.property_rent), pad=(5, 5), size=(20, 1))
          ]
        )
        Col.append([sg.HSeparator()])
        Col.append(
          [
            sg.Text('Imposto federal:', pad=(5, 5), size=(20, 1)),
            sg.Text(str(prop.federal_tax), pad=(5, 5), size=(20, 1))
          ]
        )
  layout.append([sg.Text('Mostrando informações', pad=(5, 5), size=(25, 1))])
  layout.append([sg.Column(Col, element_justification='c', scrollable=True, vertical_scroll_only=True)])
  layout.append([sg.Button('Sair', size=(15, 1), button_color=('white', 'firebrick3'))])
  window = sg.Window("Mostrando Todos Apartamentos", layout, element_justification='c', resizable=True, finalize=True,
                     modal=True)
  window.TKroot.minsize(320, 240)
  while True:
    event, values = window.read(close=True)
    if event in ["Exit", sg.WIN_CLOSED, "Sair"]:
      break
  window.close()


# Mostra apenas casas.
def show_home_property(property_list):
  layout = []
  Col = []
  if None in property_list:
    result_window('Erro, existe NULL no vetor.')
    return False
  for prop in property_list:
    if prop is not None and isinstance(prop, ResidentialHome):
      # layout da página.
      Col.append([sg.HSeparator()])
      Col.append([
        sg.Text('ID:', pad=(5, 5), size=(20, 1)),  # Label
        sg.Text(str(prop.property_code), pad=(5, 5), size=(20, 1))  # Valor do obj.
      ])
      Col.append(
        [
          sg.Text('Endereço: ', pad=(5, 5), size=(20, 1)),
          sg.Text(str(prop.address), pad=(5, 5), size=(20, 1))
        ]
      )
      Col.append(
        [
          sg.Text('Data de construção:', pad=(5, 5), size=(20, 1)),
          sg.Text(str(prop.construction_date), pad=(5, 5), size=(20, 1))
        ]
      )
      Col.append(
        [
          sg.Text('Área total:', pad=(5, 5), size=(20, 1)),
          sg.Text(str(prop.total_area), pad=(5, 5), size=(20, 1))
        ]
      )
      Col.append(
        [
          sg.Text('Área de construção:', pad=(5, 5), size=(20, 1)),
          sg.Text(str(prop.constructed_area), pad=(5, 5), size=(20, 1))
        ]
      )
      Col.append(
        [
          sg.Text('Num. de quartos:', pad=(5, 5), size=(20, 1)),
          sg.Text(str(prop.num_rooms), pad=(5, 5), size=(20, 1))
        ]
      )
      Col.append(
        [
          sg.Text('Num. de banheiros:', pad=(5, 5), size=(20, 1)),
          sg.Text(str(prop.num_bathrooms), pad=(5, 5), size=(20, 1))
        ]
      )
      Col.append(
        [
          sg.Text('Num. de vagas:', pad=(5, 5), size=(20, 1)),
          sg.Text(str(prop.num_spots_garage), pad=(5, 5), size=(20, 1))
        ]
      )
      Col.append(
        [
          sg.Text('IPTU:', pad=(5, 5), size=(20, 1)),
          sg.Text(str(prop.iptu), pad=(5, 5), size=(20, 1))
        ]
      )
      Col.append(
        [
          sg.Text('Valor propriedade:', pad=(5, 5), size=(20, 1)),
          sg.Text(str(prop.property_worth), pad=(5, 5), size=(20, 1))
        ]
      )
      Col.append(
        [
          sg.Text('Valor de aluguel:', pad=(5, 5), size=(20, 1)),
          sg.Text(str(prop.property_rent), pad=(5, 5), size=(20, 1))
        ]
      )
      Col.append([sg.HSeparator()])
  layout.append([sg.Text('Mostrando informações', pad=(5, 5), size=(25, 1))])
  layout.append([sg.Column(Col, element_justification='c', scrollable=True, vertical_scroll_only=True)])
  layout.append([sg.Button('Sair', size=(15, 1), button_color=('white', 'firebrick3'))])
  window = sg.Window("Mostrando Todos Apartamentos", layout, element_justification='c', resizable=True, finalize=True,
                     modal=True)
  window.TKroot.minsize(320, 240)
  while True:
    event, values = window.read(close=True)
    if event in ["Exit", sg.WIN_CLOSED, "Sair"]:
      break
  window.close()


def show_all_property(property_list):
  layout = []
  Col = []
  if None in property_list:
    result_window('Erro, existe NULL no vetor.')
    return False
  for prop in property_list:
    if prop is not None:
      # layout da página.
      Col.append(
        [
          sg.Text('Imóvel:', pad=(5, 5), size=(20, 1)),
        ]
      )
      Col.append([sg.HSeparator()])
      Col.append([
        sg.Text('ID:', pad=(5, 5), size=(20, 1)),  # Label
        sg.Text(str(prop.property_code), pad=(5, 5), size=(20, 1))  # Valor do obj.
      ])
      Col.append(
        [
          sg.Text('Endereço: ', pad=(5, 5), size=(20, 1)),
          sg.Text(str(prop.address), pad=(5, 5), size=(20, 1))
        ]
      )
      Col.append(
        [
          sg.Text('Data de construção:', pad=(5, 5), size=(20, 1)),
          sg.Text(str(prop.construction_date), pad=(5, 5), size=(20, 1))
        ]
      )
      Col.append(
        [
          sg.Text('Área total:', pad=(5, 5), size=(20, 1)),
          sg.Text(str(prop.total_area), pad=(5, 5), size=(20, 1))
        ]
      )
      Col.append(
        [
          sg.Text('Área de construção:', pad=(5, 5), size=(20, 1)),
          sg.Text(str(prop.constructed_area), pad=(5, 5), size=(20, 1))
        ]
      )
      Col.append(
        [
          sg.Text('Num. de quartos:', pad=(5, 5), size=(20, 1)),
          sg.Text(str(prop.num_rooms), pad=(5, 5), size=(20, 1))
        ]
      )
      Col.append(
        [
          sg.Text('Num. de banheiros:', pad=(5, 5), size=(20, 1)),
          sg.Text(str(prop.num_bathrooms), pad=(5, 5), size=(20, 1))
        ]
      )
      Col.append(
        [
          sg.Text('Num. de vagas:', pad=(5, 5), size=(20, 1)),
          sg.Text(str(prop.num_spots_garage), pad=(5, 5), size=(20, 1))
        ]
      )
      Col.append(
        [
          sg.Text('IPTU:', pad=(5, 5), size=(20, 1)),
          sg.Text(str(prop.iptu), pad=(5, 5), size=(20, 1))
        ]
      )
      Col.append(
        [
          sg.Text('Valor propriedade:', pad=(5, 5), size=(20, 1)),
          sg.Text(str(prop.property_worth), pad=(5, 5), size=(20, 1))
        ]
      )
      Col.append(
        [
          sg.Text('Valor de aluguel:', pad=(5, 5), size=(20, 1)),
          sg.Text(str(prop.property_rent), pad=(5, 5), size=(20, 1))
        ]
      )
      Col.append([sg.HSeparator()])
      if isinstance(prop, ResidentialApartment):
        Col.append(
          [
            sg.Text('Apartamento:', pad=(5, 5), size=(20, 1)),
          ]
        )
        Col.append(
          [
            sg.Text('Andar do ap:', pad=(5, 5), size=(20, 1)),
            sg.Text(str(prop.apartment_value), pad=(5, 5), size=(20, 1))
          ]
        )
        Col.append(
          [
            sg.Text('Valor do ap:', pad=(5, 5), size=(20, 1)),
            sg.Text(str(prop.apartment_value), pad=(5, 5), size=(20, 1))
          ]
        )
      elif isinstance(prop, Comercial):
        Col.append(
          [
            sg.Text('Comércio:', pad=(5, 5), size=(20, 1)),
          ]
        )
        Col.append(
          [
            sg.Text('Imposto federal:', pad=(5, 5), size=(20, 1)),
            sg.Text(str(prop.federal_tax), pad=(5, 5), size=(20, 1))
          ]
        )
  layout.append([sg.Text('Mostrando informações', pad=(5, 5), size=(25, 1))])
  layout.append([sg.Column(Col, size=(640, 480), element_justification='c', scrollable=True)])
  layout.append([sg.Button('Sair', size=(15, 1), button_color=('white', 'firebrick3'))])
  window = sg.Window("Mostrando Todos Apartamentos", layout, size=(640, 480), element_justification='c', resizable=True,
                     finalize=True, modal=True)
  window.TKroot.minsize(320, 240)
  while True:
    event, values = window.read(close=True)
    if event in ["Exit", sg.WIN_CLOSED, "Sair"]:
      break
  window.close()

def show_all_insurance(insurance_list: list):
  print(insurance_list)
  Col = []
  Col.append([sg.Text('Mostrando informações')])
  for i in insurance_list:
    if i is not None:
      if isinstance(i, Insurance):
        # layout da página.
        Col.append([sg.HSeparator()])
        Col.append([
          sg.Text('ID:', pad=(5, 5), size=(20, 1)),  # Label
          sg.Text(str(i.insurance_code), pad=(5, 5), size=(20, 1))  # Valor do obj.
        ])
        Col.append([
          sg.Text('Nome Seguradora:', pad=(5, 5), size=(20, 1)),  # Label
          sg.Text(str(i.insurance_name), pad=(5, 5), size=(20, 1))  # Valor do obj.
        ])
        Col.append([
          sg.Text('Tipo:', pad=(5, 5), size=(20, 1)),  # Label
          sg.Text(str(i.insurance_type), pad=(5, 5), size=(20, 1))  # Valor do obj.
        ])
        Col.append([
          sg.Text('Descrição:', pad=(5, 5), size=(20, 1)),  # Label
          sg.Text(str(i.insurance_desc), pad=(5, 5), size=(20, 1))  # Valor do obj.
        ])
        Col.append([
          sg.Text('Preço:', pad=(5, 5), size=(20, 1)),  # Label
          sg.Text(str(i.insurance_value), pad=(5, 5), size=(20, 1))  # Valor do obj.
        ])
      Col.append([sg.HSeparator()])
  layout = []
  layout.append([sg.Column(Col, element_justification='c', scrollable=True, vertical_scroll_only=True)])
  layout.append([sg.Button('Sair', size=(15, 1), button_color=('white', 'firebrick3'))])
  window = sg.Window("Mostrando Todos Clientes", layout, element_justification='c', resizable=True, finalize=True,
                     modal=True)
  window.TKroot.minsize(320, 240)
  while True:
    event, values = window.read(close=True)
    if event in ["Exit", sg.WIN_CLOSED, "Sair"]:
      break
  window.close()

# FIM Mostrar Objetos
