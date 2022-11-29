import PySimpleGUI as sg
import sys

from datetime import datetime
from classes.money.insurance import Insurance
from classes.money.payment_method_card import PaymentByCard
from classes.money.payment_method_money import PaymentByMoney
from classes.property.comercial import Comercial
from classes.property.residential_home import ResidentialHome

# import de classes
sys.path.append('../')
from classes.user.user_client import UserClient
from classes.user.user_broker import UserBroker
from classes.property.residential_apartment import ResidentialApartment
from classes.sales.sales import Sale


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
def show_users_client(user_list: list) -> None:
    print(user_list)
    layout = []
    Col = []
    if None in user_list:
        result_window('Erro, existe NULL no vetor.')
        return False
    for user in user_list:
        if user is not None:
            if isinstance(user, UserClient):
                # layout da página.
                Col.append([sg.HSeparator()])
                Col.append([
                    sg.Text('ID:', pad=(5, 5), size=(20, 1)),  # Label
                    sg.Text(str(user.user_code), pad=(5, 5), size=(45, 1))  # Valor do obj.
                ])
                Col.append(
                    [
                        sg.Text('Nome: ', pad=(5, 5), size=(20, 1)),
                        sg.Text(str(user.name), pad=(5, 5), size=(45, 1))
                    ]
                )
                Col.append(
                    [
                        sg.Text('CPF:', pad=(5, 5), size=(20, 1)),
                        sg.Text(str(user.cpf), pad=(5, 5), size=(45, 1))
                    ]
                )
                Col.append(
                    [
                        sg.Text('RG:', pad=(5, 5), size=(20, 1)),
                        sg.Text(str(user.rg), pad=(5, 5), size=(45, 1))
                    ]
                )
                Col.append(
                    [
                        sg.Text('Ano de nascimento:', pad=(5, 5), size=(20, 1)),
                        sg.Text(str(user.anniversary_date), pad=(5, 5), size=(45, 1))
                    ]
                )
                Col.append(
                    [
                        sg.Text('Endereço:', pad=(5, 5), size=(20, 1)),
                        sg.Text(str(user.address), pad=(5, 5), size=(45, 1))
                    ]
                )
                Col.append(
                    [
                        sg.Text('CEP:', pad=(5, 5), size=(20, 1)),
                        sg.Text(str(user.cep), pad=(5, 5), size=(45, 1))
                    ]
                )
                Col.append(
                    [
                        sg.Text('Telefone:', pad=(5, 5), size=(20, 1)),
                        sg.Text(str(user.phone), pad=(5, 5), size=(45, 1))
                    ]
                )
                Col.append(
                    [
                        sg.Text('Email:', pad=(5, 5), size=(20, 1)),
                        sg.Text(str(user.email), pad=(5, 5), size=(45, 1))
                    ]
                )
                Col.append(
                    [
                        sg.Text('Data de registro:', pad=(5, 5), size=(20, 1)),
                        sg.Text(str(user.register_date), pad=(5, 5), size=(45, 1))
                    ]
                )
                Col.append([sg.HSeparator()])
    layout.append([sg.Text('Mostrando informações', pad=(5, 5), size=(25, 1))])
    layout.append(
        [sg.Column(Col, size=(640, 800), element_justification='c', scrollable=True, vertical_scroll_only=True)])
    layout.append([sg.Button('Sair', size=(15, 1), button_color=('white', 'firebrick3'))])
    window = sg.Window("Mostrando Todos os Clientes", layout, element_justification='c', resizable=True, finalize=True,
                       modal=True)
    window.TKroot.minsize(320, 240)
    while True:
        event, values = window.read(close=True)
        if event in ["Exit", sg.WIN_CLOSED, "Sair"]:
            break
    window.close()


  # Mostrando os corretores.
def show_users_broker(user_list: list) -> None:
  print(user_list)
  layout = []
  Col = []
  if None in user_list:
    result_window('Erro, existe NULL no vetor.')
    return False
  for user in user_list:
    if user is not None:
      if isinstance(user, UserBroker):
        # layout da página.
        Col.append([sg.HSeparator()])
        Col.append([
          sg.Text('ID:', pad=(5, 5), size=(20, 1)),  # Label
          sg.Text(str(user.user_code), pad=(5, 5), size=(45, 1))  # Valor do obj.
        ])
        Col.append(
          [
            sg.Text('Nome: ', pad=(5, 5), size=(20, 1)),
            sg.Text(str(user.name), pad=(5, 5), size=(45, 1))
          ]
        )
        Col.append(
          [
            sg.Text('CPF:', pad=(5, 5), size=(20, 1)),
            sg.Text(str(user.cpf), pad=(5, 5), size=(45, 1))
          ]
        )
        Col.append(
          [
            sg.Text('RG:', pad=(5, 5), size=(20, 1)),
            sg.Text(str(user.rg), pad=(5, 5), size=(45, 1))
          ]
        )
        Col.append(
          [
            sg.Text('Ano de nascimento:', pad=(5, 5), size=(20, 1)),
            sg.Text(str(user.anniversary_date), pad=(5, 5), size=(45, 1))
          ]
        )
        Col.append(
          [
            sg.Text('Endereço:', pad=(5, 5), size=(20, 1)),
            sg.Text(str(user.address), pad=(5, 5), size=(45, 1))
          ]
        )
        Col.append(
          [
            sg.Text('CEP:', pad=(5, 5), size=(20, 1)),
            sg.Text(str(user.cep), pad=(5, 5), size=(45, 1))
          ]
        )
        Col.append(
          [
            sg.Text('Telefone:', pad=(5, 5), size=(20, 1)),
            sg.Text(str(user.phone), pad=(5, 5), size=(45, 1))
          ]
        )
        Col.append(
          [
            sg.Text('Email:', pad=(5, 5), size=(20, 1)),
            sg.Text(str(user.email), pad=(5, 5), size=(45, 1))
          ]
        )
        Col.append(
          [
            sg.Text('Crescimento:', pad=(5, 5), size=(20, 1)),
            sg.Text(str(user.growf), pad=(5, 5), size=(45, 1))
          ]
        )
        Col.append(
          [
            sg.Text('Salário:', pad=(5, 5), size=(20, 1)),
            sg.Text(str(user.wage), pad=(5, 5), size=(45, 1))
          ]
        )
        Col.append(
          [
            sg.Text('PIS:', pad=(5, 5), size=(20, 1)),
            sg.Text(str(user.pis), pad=(5, 5), size=(45, 1))
          ]
        )
        Col.append(
          [
            sg.Text('Data de admissão:', pad=(5, 5), size=(20, 1)),
            sg.Text(str(user.hired_date), pad=(5, 5), size=(45, 1))
          ]
        )
        Col.append([sg.HSeparator()])
  layout.append([sg.Text('Mostrando informações', pad=(5, 5), size=(25, 1))])
  layout.append([sg.Column(Col, size=(640, 800), element_justification='c', scrollable=True, vertical_scroll_only=True)])
  layout.append([sg.Button('Sair', size=(15, 1), button_color=('white', 'firebrick3'))])
  window = sg.Window("Mostrando Todos os Corretores", layout, element_justification='c', resizable=True, finalize=True,
                     modal=True)
  window.TKroot.minsize(320, 240)
  while True:
    event, values = window.read(close=True)
    if event in ["Exit", sg.WIN_CLOSED, "Sair"]:
      break
  window.close()


# Mostrar Apartamentos


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
        sg.Text(str(prop.property_code), pad=(5, 5), size=(45, 1))  # Valor do obj.
      ])
      Col.append(
        [
          sg.Text('Endereço: ', pad=(5, 5), size=(20, 1)),
          sg.Text(str(prop.address), pad=(5, 5), size=(45, 1))
        ]
      )
      Col.append(
        [
          sg.Text('Data de construção:', pad=(5, 5), size=(20, 1)),
          sg.Text(str(prop.construction_date), pad=(5, 5), size=(45, 1))
        ]
      )
      Col.append(
        [
          sg.Text('Área total:', pad=(5, 5), size=(20, 1)),
          sg.Text(str(prop.total_area), pad=(5, 5), size=(45, 1))
        ]
      )
      Col.append(
        [
          sg.Text('Área de construção:', pad=(5, 5), size=(20, 1)),
          sg.Text(str(prop.constructed_area), pad=(5, 5), size=(45, 1))
        ]
      )
      Col.append(
        [
          sg.Text('Num. de quartos:', pad=(5, 5), size=(20, 1)),
          sg.Text(str(prop.num_rooms), pad=(5, 5), size=(45, 1))
        ]
      )
      Col.append(
        [
          sg.Text('Num. de banheiros:', pad=(5, 5), size=(20, 1)),
          sg.Text(str(prop.num_bathrooms), pad=(5, 5), size=(45, 1))
        ]
      )
      Col.append(
        [
          sg.Text('Num. de vagas:', pad=(5, 5), size=(20, 1)),
          sg.Text(str(prop.num_spots_garage), pad=(5, 5), size=(45, 1))
        ]
      )
      Col.append(
        [
          sg.Text('IPTU:', pad=(5, 5), size=(20, 1)),
          sg.Text(str(prop.iptu), pad=(5, 5), size=(45, 1))
        ]
      )
      Col.append(
        [
          sg.Text('Valor propriedade:', pad=(5, 5), size=(20, 1)),
          sg.Text(str(prop.property_worth), pad=(5, 5), size=(45, 1))
        ]
      )
      Col.append(
        [
          sg.Text('Valor de aluguel:', pad=(5, 5), size=(20, 1)),
          sg.Text(str(prop.property_rent), pad=(5, 5), size=(45, 1))
        ]
      )
      Col.append([sg.HSeparator()])
      if isinstance(prop, ResidentialApartment):
        Col.append(
          [
            sg.Text('Andar do ap:', pad=(5, 5), size=(20, 1)),
            sg.Text(str(prop.apartment_value), pad=(5, 5), size=(45, 1))
          ]
        )
        Col.append(
          [
            sg.Text('Valor do ap:', pad=(5, 5), size=(20, 1)),
            sg.Text(str(prop.apartment_value), pad=(5, 5), size=(45, 1))
          ]
        )
      if isinstance(prop, Comercial):
        Col.append(
          [
            sg.Text('Imposto federal:', pad=(5, 5), size=(20, 1)),
            sg.Text(str(prop.federal_tax), pad=(5, 5), size=(45, 1))
          ]
        )
  layout.append([sg.Text('Mostrando informações', pad=(5, 5), size=(25, 1))])
  layout.append([sg.Column(Col, size=(640, 800), element_justification='c', scrollable=True, vertical_scroll_only=True)])
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
          sg.Text(str(prop.property_code), pad=(5, 5), size=(45, 1))  # Valor do obj.
        ])
        Col.append(
          [
            sg.Text('Endereço: ', pad=(5, 5), size=(20, 1)),
            sg.Text(str(prop.address), pad=(5, 5), size=(45, 1))
          ]
        )
        Col.append(
          [
            sg.Text('Data de construção:', pad=(5, 5), size=(20, 1)),
            sg.Text(str(prop.construction_date), pad=(5, 5), size=(45, 1))
          ]
        )
        Col.append(
          [
            sg.Text('Área total:', pad=(5, 5), size=(20, 1)),
            sg.Text(str(prop.total_area), pad=(5, 5), size=(45, 1))
          ]
        )
        Col.append(
          [
            sg.Text('Área de construção:', pad=(5, 5), size=(20, 1)),
            sg.Text(str(prop.constructed_area), pad=(5, 5), size=(45, 1))
          ]
        )
        Col.append(
          [
            sg.Text('Num. de quartos:', pad=(5, 5), size=(20, 1)),
            sg.Text(str(prop.num_rooms), pad=(5, 5), size=(45, 1))
          ]
        )
        Col.append(
          [
            sg.Text('Num. de banheiros:', pad=(5, 5), size=(20, 1)),
            sg.Text(str(prop.num_bathrooms), pad=(5, 5), size=(45, 1))
          ]
        )
        Col.append(
          [
            sg.Text('Num. de vagas:', pad=(5, 5), size=(20, 1)),
            sg.Text(str(prop.num_spots_garage), pad=(5, 5), size=(45, 1))
          ]
        )
        Col.append(
          [
            sg.Text('IPTU:', pad=(5, 5), size=(20, 1)),
            sg.Text(str(prop.iptu), pad=(5, 5), size=(45, 1))
          ]
        )
        Col.append(
          [
            sg.Text('Valor propriedade:', pad=(5, 5), size=(20, 1)),
            sg.Text(str(prop.property_worth), pad=(5, 5), size=(45, 1))
          ]
        )
        Col.append(
          [
            sg.Text('Valor de aluguel:', pad=(5, 5), size=(20, 1)),
            sg.Text(str(prop.property_rent), pad=(5, 5), size=(45, 1))
          ]
        )
        Col.append([sg.HSeparator()])
        Col.append(
          [
            sg.Text('Andar do ap:', pad=(5, 5), size=(20, 1)),
            sg.Text(str(prop.floor), pad=(5, 5), size=(45, 1))
          ]
        )
        Col.append(
          [
            sg.Text('Valor do condomínio:', pad=(5, 5), size=(20, 1)),
            sg.Text(str(prop.apartment_value), pad=(5, 5), size=(45, 1))
          ]
        )
  layout.append([sg.Text('Mostrando informações', pad=(5, 5), size=(25, 1))])
  layout.append([sg.Column(Col, size=(640, 800), element_justification='c', scrollable=True, vertical_scroll_only=True)])
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
          sg.Text(str(prop.property_code), pad=(5, 5), size=(45, 1))  # Valor do obj.
        ])
        Col.append(
          [
            sg.Text('Endereço: ', pad=(5, 5), size=(20, 1)),
            sg.Text(str(prop.address), pad=(5, 5), size=(45, 1))
          ]
        )
        Col.append(
          [
            sg.Text('Data de construção:', pad=(5, 5), size=(20, 1)),
            sg.Text(str(prop.construction_date), pad=(5, 5), size=(45, 1))
          ]
        )
        Col.append(
          [
            sg.Text('Área total:', pad=(5, 5), size=(20, 1)),
            sg.Text(str(prop.total_area), pad=(5, 5), size=(45, 1))
          ]
        )
        Col.append(
          [
            sg.Text('Área de construção:', pad=(5, 5), size=(20, 1)),
            sg.Text(str(prop.constructed_area), pad=(5, 5), size=(45, 1))
          ]
        )
        Col.append(
          [
            sg.Text('Num. de quartos:', pad=(5, 5), size=(20, 1)),
            sg.Text(str(prop.num_rooms), pad=(5, 5), size=(45, 1))
          ]
        )
        Col.append(
          [
            sg.Text('Num. de banheiros:', pad=(5, 5), size=(20, 1)),
            sg.Text(str(prop.num_bathrooms), pad=(5, 5), size=(45, 1))
          ]
        )
        Col.append(
          [
            sg.Text('Num. de vagas:', pad=(5, 5), size=(20, 1)),
            sg.Text(str(prop.num_spots_garage), pad=(5, 5), size=(45, 1))
          ]
        )
        Col.append(
          [
            sg.Text('IPTU:', pad=(5, 5), size=(20, 1)),
            sg.Text(str(prop.iptu), pad=(5, 5), size=(45, 1))
          ]
        )
        Col.append(
          [
            sg.Text('Valor propriedade:', pad=(5, 5), size=(20, 1)),
            sg.Text(str(prop.property_worth), pad=(5, 5), size=(45, 1))
          ]
        )
        Col.append(
          [
            sg.Text('Valor de aluguel:', pad=(5, 5), size=(20, 1)),
            sg.Text(str(prop.property_rent), pad=(5, 5), size=(45, 1))
          ]
        )
        Col.append([sg.HSeparator()])
        Col.append(
          [
            sg.Text('Imposto federal:', pad=(5, 5), size=(20, 1)),
            sg.Text(str(prop.federal_tax), pad=(5, 5), size=(45, 1))
          ]
        )
  layout.append([sg.Text('Mostrando informações', pad=(5, 5), size=(25, 1))])
  layout.append([sg.Column(Col, size=(640, 800), element_justification='c', scrollable=True, vertical_scroll_only=True)])
  layout.append([sg.Button('Sair', size=(15, 1), button_color=('white', 'firebrick3'))])
  window = sg.Window("Mostrando todos os Comércios", layout, element_justification='c', resizable=True, finalize=True,
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
                sg.Text(str(prop.property_code), pad=(5, 5), size=(45, 1))  # Valor do obj.
            ])
            Col.append(
                [
                    sg.Text('Endereço: ', pad=(5, 5), size=(20, 1)),
                    sg.Text(str(prop.address), pad=(5, 5), size=(45, 1))
                ]
            )
            Col.append(
                [
                    sg.Text('Data de construção:', pad=(5, 5), size=(20, 1)),
                    sg.Text(str(prop.construction_date), pad=(5, 5), size=(45, 1))
                ]
            )
            Col.append(
                [
                    sg.Text('Área total:', pad=(5, 5), size=(20, 1)),
                    sg.Text(str(prop.total_area), pad=(5, 5), size=(45, 1))
                ]
            )
            Col.append(
                [
                    sg.Text('Área de construção:', pad=(5, 5), size=(20, 1)),
                    sg.Text(str(prop.constructed_area), pad=(5, 5), size=(45, 1))
                ]
            )
            Col.append(
                [
                    sg.Text('Num. de quartos:', pad=(5, 5), size=(20, 1)),
                    sg.Text(str(prop.num_rooms), pad=(5, 5), size=(45, 1))
                ]
            )
            Col.append(
                [
                    sg.Text('Num. de banheiros:', pad=(5, 5), size=(20, 1)),
                    sg.Text(str(prop.num_bathrooms), pad=(5, 5), size=(45, 1))
                ]
            )
            Col.append(
                [
                    sg.Text('Num. de vagas:', pad=(5, 5), size=(20, 1)),
                    sg.Text(str(prop.num_spots_garage), pad=(5, 5), size=(45, 1))
                ]
            )
            Col.append(
                [
                    sg.Text('IPTU:', pad=(5, 5), size=(20, 1)),
                    sg.Text(str(prop.iptu), pad=(5, 5), size=(45, 1))
                ]
            )
            Col.append(
                [
                    sg.Text('Valor propriedade:', pad=(5, 5), size=(20, 1)),
                    sg.Text(str(prop.property_worth), pad=(5, 5), size=(45, 1))
                ]
            )
            Col.append(
                [
                    sg.Text('Valor de aluguel:', pad=(5, 5), size=(20, 1)),
                    sg.Text(str(prop.property_rent), pad=(5, 5), size=(45, 1))
                ]
            )
            Col.append([sg.HSeparator()])
    layout.append([sg.Text('Mostrando informações', pad=(5, 5), size=(25, 1))])
    layout.append(
        [sg.Column(Col, size=(640, 800), element_justification='c', scrollable=True, vertical_scroll_only=True)])
    layout.append([sg.Button('Sair', size=(15, 1), button_color=('white', 'firebrick3'))])
    window = sg.Window("Mostrando Todos as Casas", layout, element_justification='c', resizable=True, finalize=True,
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
                sg.Text(str(prop.property_code), pad=(5, 5), size=(45, 1))  # Valor do obj.
            ])
            Col.append(
                [
                    sg.Text('Endereço: ', pad=(5, 5), size=(20, 1)),
                    sg.Text(str(prop.address), pad=(5, 5), size=(45, 1))
                ]
            )
            Col.append(
                [
                    sg.Text('Data de construção:', pad=(5, 5), size=(20, 1)),
                    sg.Text(str(prop.construction_date), pad=(5, 5), size=(45, 1))
                ]
            )
            Col.append(
                [
                    sg.Text('Área total:', pad=(5, 5), size=(20, 1)),
                    sg.Text(str(prop.total_area), pad=(5, 5), size=(45, 1))
                ]
            )
            Col.append(
                [
                    sg.Text('Área de construção:', pad=(5, 5), size=(20, 1)),
                    sg.Text(str(prop.constructed_area), pad=(5, 5), size=(45, 1))
                ]
            )
            Col.append(
                [
                    sg.Text('Num. de quartos:', pad=(5, 5), size=(20, 1)),
                    sg.Text(str(prop.num_rooms), pad=(5, 5), size=(45, 1))
                ]
            )
            Col.append(
                [
                    sg.Text('Num. de banheiros:', pad=(5, 5), size=(20, 1)),
                    sg.Text(str(prop.num_bathrooms), pad=(5, 5), size=(45, 1))
                ]
            )
            Col.append(
                [
                    sg.Text('Num. de vagas:', pad=(5, 5), size=(20, 1)),
                    sg.Text(str(prop.num_spots_garage), pad=(5, 5), size=(45, 1))
                ]
            )
            Col.append(
                [
                    sg.Text('IPTU:', pad=(5, 5), size=(20, 1)),
                    sg.Text(str(prop.iptu), pad=(5, 5), size=(45, 1))
                ]
            )
            Col.append(
                [
                    sg.Text('Valor propriedade:', pad=(5, 5), size=(20, 1)),
                    sg.Text(str(prop.property_worth), pad=(5, 5), size=(45, 1))
                ]
            )
            Col.append(
                [
                    sg.Text('Valor de aluguel:', pad=(5, 5), size=(20, 1)),
                    sg.Text(str(prop.property_rent), pad=(5, 5), size=(45, 1))
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
                        sg.Text(str(prop.apartment_value), pad=(5, 5), size=(45, 1))
                    ]
                )
                Col.append(
                    [
                        sg.Text('Valor do ap:', pad=(5, 5), size=(20, 1)),
                        sg.Text(str(prop.apartment_value), pad=(5, 5), size=(45, 1))
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
                        sg.Text(str(prop.federal_tax), pad=(5, 5), size=(45, 1))
                    ]
                )
    layout.append([sg.Text('Mostrando informações', pad=(5, 5), size=(25, 1))])
    layout.append(
        [sg.Column(Col, size=(640, 800), element_justification='c', scrollable=True, vertical_scroll_only=True)])
    layout.append([sg.Button('Sair', size=(15, 1), button_color=('white', 'firebrick3'))])
    window = sg.Window("Mostrando Todos os Imóveis", layout, element_justification='c', resizable=True, finalize=True,
                       modal=True)
    window.TKroot.minsize(320, 240)
    while True:
        event, values = window.read(close=True)
        if event in ["Exit", sg.WIN_CLOSED, "Sair"]:
            break
    window.close()


def show_all_payment_methods(payment_list) -> object:
    payment: object = None
    layout = []
    Col = []
    if None in payment_list:
        result_window('Erro, existe NULL/None no vetor.')
        return False
    for payment in payment_list:
        Col.append([sg.HSeparator()])
        Col.append(
            [
                sg.Text('ID:', pad=(5, 5), size=(20, 1)),
                sg.Text(str(payment.payment_code), pad=(5, 5), size=(45, 1))
            ]
        )
        Col.append(
            [
                sg.Text('Tipo de pagamento:', pad=(5, 5), size=(20, 1)),
                sg.Text(str(payment.payment_type), pad=(5, 5), size=(45, 1))
            ]
        )
        if isinstance(payment, PaymentByMoney):
            Col.append(
                [
                    sg.Text('Quantia:', pad=(5, 5), size=(20, 1)),
                    sg.Text(str(payment.total_charge), pad=(5, 5), size=(45, 1))
                ]
            )
        elif isinstance(payment, PaymentByCard):
            Col.append(
                [
                    sg.Text('Nome no cartão:', pad=(5, 5), size=(20, 1)),
                    sg.Text(str(payment.card_name), pad=(5, 5), size=(45, 1))
                ]
            )
            Col.append(
                [
                    sg.Text('Bandeira:', pad=(5, 5), size=(20, 1)),
                    sg.Text(str(payment.flag), pad=(5, 5), size=(45, 1))
                ]
            )
            Col.append(
                [
                    sg.Text('Número do cartão:', pad=(5, 5), size=(20, 1)),
                    sg.Text(str(payment.number), pad=(5, 5), size=(45, 1))
                ]
            )
            Col.append([sg.HSeparator()])
    layout.append([sg.Text('Mostrando informações', pad=(5, 5), size=(25, 1))])
    layout.append(
        [sg.Column(Col, size=(640, 800), element_justification='c', scrollable=True, vertical_scroll_only=True)])
    layout.append([sg.Button('Sair', size=(15, 1), button_color=('white', 'firebrick3'))])
    window = sg.Window("Mostrando Todos os métodos de pagamento", layout, element_justification='c',
                       resizable=True, finalize=True,
                       modal=True)
    window.TKroot.minsize(320, 240)
    while True:
        event, values = window.read(close=True)
        if event in ["Exit", sg.WIN_CLOSED, "Sair"]:
            break
    window.close()


def show_all_payment_money(payment_list) -> object:
    layout = []
    Col = []
    if None in payment_list:
        result_window('Erro, existe NULL/None no vetor.')
        return False
    for payment in payment_list:
        if isinstance(payment, PaymentByMoney):
            Col.append([sg.HSeparator()])
            Col.append(
                [
                    sg.Text('ID:', pad=(5, 5), size=(20, 1)),
                    sg.Text(str(payment.payment_code), pad=(5, 5), size=(45, 1))
                ]
            )
            Col.append(
                [
                    sg.Text('Quantia:', pad=(5, 5), size=(20, 1)),
                    sg.Text(str(payment.total_charge), pad=(5, 5), size=(45, 1))
                ]
            )
            Col.append([sg.HSeparator()])
    layout.append([sg.Text('Mostrando informações', pad=(5, 5), size=(25, 1))])
    layout.append(
        [sg.Column(Col, size=(640, 800), element_justification='c', scrollable=True, vertical_scroll_only=True)])
    layout.append([sg.Button('Sair', size=(15, 1), button_color=('white', 'firebrick3'))])
    window = sg.Window("Mostrando todos pagamentos com dinheiro", layout, element_justification='c', resizable=True,
                       finalize=True,
                       modal=True)
    window.TKroot.minsize(320, 240)
    while True:
        event, values = window.read(close=True)
        if event in ["Exit", sg.WIN_CLOSED, "Sair"]:
            break
    window.close()


def show_all_payment_card(payment_list) -> object:
    layout = []
    Col = []
    if None in payment_list:
        result_window('Erro, existe NULL/None no vetor.')
        return False
    for payment in payment_list:
        if isinstance(payment, PaymentByCard):
            Col.append([sg.HSeparator()])
            Col.append(
                [
                    sg.Text('ID:', pad=(5, 5), size=(20, 1)),
                    sg.Text(str(payment.payment_code), pad=(5, 5), size=(45, 1))
                ]
            )
            Col.append(
                [
                    sg.Text('Nome no cartão:', pad=(5, 5), size=(20, 1)),
                    sg.Text(str(payment.card_name), pad=(5, 5), size=(45, 1))
                ]
            )
            Col.append(
                [
                    sg.Text('Bandeira:', pad=(5, 5), size=(20, 1)),
                    sg.Text(str(payment.flag), pad=(5, 5), size=(45, 1))
                ]
            )
            Col.append(
                [
                    sg.Text('Número do cartão:', pad=(5, 5), size=(20, 1)),
                    sg.Text(str(payment.number), pad=(5, 5), size=(45, 1))
                ]
            )
            Col.append([sg.HSeparator()])
    layout.append([sg.Text('Mostrando informações', pad=(5, 5), size=(25, 1))])
    layout.append(
        [sg.Column(Col, size=(640, 800), element_justification='c', scrollable=True, vertical_scroll_only=True)])
    layout.append([sg.Button('Sair', size=(15, 1), button_color=('white', 'firebrick3'))])
    window = sg.Window("Mostrando mostrando os pagamentos por cartão", layout, element_justification='c',
                       resizable=True, finalize=True,
                       modal=True)
    window.TKroot.minsize(320, 240)
    while True:
        event, values = window.read(close=True)
        if event in ["Exit", sg.WIN_CLOSED, "Sair"]:
            break
    window.close()


def show_all_insurance(insurance_list: list):
    print(insurance_list)
    Col = []
    for i in insurance_list:
        if i is not None:
            if isinstance(i, Insurance):
                # layout da página.
                Col.append([sg.HSeparator()])
                Col.append([
                    sg.Text('ID:', pad=(5, 5), size=(20, 1)),  # Label
                    sg.Text(str(i.insurance_code), pad=(5, 5), size=(45, 1))  # Valor do obj.
                ])
                Col.append([
                    sg.Text('Nome Seguradora:', pad=(5, 5), size=(20, 1)),  # Label
                    sg.Text(str(i.insurance_name), pad=(5, 5), size=(45, 1))  # Valor do obj.
                ])
                Col.append([
                    sg.Text('Tipo:', pad=(5, 5), size=(20, 1)),  # Label
                    sg.Text(str(i.insurance_type), pad=(5, 5), size=(45, 1))  # Valor do obj.
                ])
                Col.append([
                    sg.Text('Descrição:', pad=(5, 5), size=(20, 1)),  # Label
                    sg.Text(str(i.insurance_desc), pad=(5, 5), size=(45, 1))  # Valor do obj.
                ])
                Col.append([
                    sg.Text('Preço:', pad=(5, 5), size=(20, 1)),  # Label
                    sg.Text(str(i.insurance_value), pad=(5, 5), size=(45, 1))  # Valor do obj.
                ])
            Col.append([sg.HSeparator()])
    layout = []
    layout.append([sg.Text('Mostrando informações', pad=(5, 5), size=(25, 1))])
    layout.append(
        [sg.Column(Col, size=(640, 800), element_justification='c', scrollable=True, vertical_scroll_only=True)])
    layout.append([sg.Button('Sair', size=(15, 1), button_color=('white', 'firebrick3'))])
    window = sg.Window("Mostrando Todos os Seguros", layout, element_justification='c', resizable=True, finalize=True,
                       modal=True)
    window.TKroot.minsize(320, 240)
    while True:
        event, values = window.read(close=True)
        if event in ["Exit", sg.WIN_CLOSED, "Sair"]:
            break
    window.close()


# Monstrando as vendas.
def show_all_sales_and_profit(obj_list: list):
  profits: float = 0.0
  Col: list = []
  for o in obj_list:
    if o is not None:
      o.print_info()
      # layout da página.
      Col.append([sg.HSeparator()])
      Col.append([
        sg.Text('ID:', pad=(5, 5), size=(20, 1)),  # Label
        sg.Text(str(o.sale_code), pad=(5, 5), size=(45, 1))  # Valor do obj.
      ])
      Col.append([
        sg.Text('Cliente:', pad=(5, 5), size=(20, 1)),  # Label
        sg.Text(str(o.client.name), pad=(5, 5), size=(45, 1))  # Valor do obj.
      ])
      Col.append([
        sg.Text('Corretor:', pad=(5, 5), size=(20, 1)),  # Label
        sg.Text(str(o.broker.name), pad=(5, 5), size=(45, 1))  # Valor do obj.
      ])
      Col.append([
        sg.Text('Imóvel:', pad=(5, 5), size=(20, 1)),  # Label
        sg.Text(str(o.sale_property.address), pad=(5, 5), size=(45, 1))  # Valor do obj.
      ])
      Col.append([
        sg.Text('Data da venda:', pad=(5, 5), size=(20, 1)),  # Label
        sg.Text(str(o.sale_date), pad=(5, 5), size=(45, 1))  # Valor do obj.
      ])
      Col.append([
        sg.Text('Preço da venda:', pad=(5, 5), size=(20, 1)),  # Label
        sg.Text(str(o.total_sale_value), pad=(5, 5), size=(45, 1))  # Valor do obj.
      ])
      Col.append([
        sg.Text('Forma de pagamento:', pad=(5, 5), size=(20, 1)),  # Label
        sg.Text(str(o.payment_method.payment_type), pad=(5, 5), size=(45, 1))  # Valor do obj.
      ])
    Col.append([sg.HSeparator()])
    profits += o.total_sale_value
  Col.append([sg.HSeparator()])
  Col.append([
    sg.Text('Lucro total:', pad=(5, 5), size=(20, 1)),  # Label
    sg.Text(str(profits), pad=(5, 5), size=(45, 1))  # Valor do obj.
  ])
  Col.append([sg.HSeparator()])
  # Inicialização da interface.
  layout = []
  layout.append([sg.Text('Mostrando informações', pad=(5, 5), size=(25, 1))])
  layout.append(
    [sg.Column(Col, size=(640, 800), element_justification='c', scrollable=True, vertical_scroll_only=True)])
  layout.append([sg.Button('Sair', size=(15, 1), button_color=('white', 'firebrick3'))])
  window = sg.Window("Mostrando todas as vendas e lucro total", layout, element_justification='c', resizable=True, finalize=True,
                     modal=True)
  window.TKroot.minsize(320, 240)
  while True:
    event, values = window.read(close=True)
    if event in ["Exit", sg.WIN_CLOSED, "Sair"]:
      break
  window.close()


def show_properties_sales(obj_list: list):
  profits: float = 0.0
  Col: list = []
  for o in obj_list:
    if o is not None:
      if o.sale_property.sale_made is True:
        o.print_info()
        # layout da página.
        Col.append([sg.HSeparator()])
        Col.append([
          sg.Text('ID:', pad=(5, 5), size=(20, 1)),  # Label
          sg.Text(str(o.sale_code), pad=(5, 5), size=(45, 1))  # Valor do obj.
        ])
        Col.append([
          sg.Text('Cliente:', pad=(5, 5), size=(20, 1)),  # Label
          sg.Text(str(o.client.name), pad=(5, 5), size=(45, 1))  # Valor do obj.
        ])
        Col.append([
          sg.Text('Corretor:', pad=(5, 5), size=(20, 1)),  # Label
          sg.Text(str(o.broker.name), pad=(5, 5), size=(45, 1))  # Valor do obj.
        ])
        Col.append([
          sg.Text('Imóvel:', pad=(5, 5), size=(20, 1)),  # Label
          sg.Text(str(o.sale_property.address), pad=(5, 5), size=(45, 1))  # Valor do obj.
        ])
        Col.append([
          sg.Text('Data da venda:', pad=(5, 5), size=(20, 1)),  # Label
          sg.Text(str(o.sale_date), pad=(5, 5), size=(45, 1))  # Valor do obj.
        ])
        Col.append([
          sg.Text('Preço da venda:', pad=(5, 5), size=(20, 1)),  # Label
          sg.Text(str(o.total_sale_value), pad=(5, 5), size=(45, 1))  # Valor do obj.
        ])
        Col.append([
          sg.Text('Forma de pagamento:', pad=(5, 5), size=(20, 1)),  # Label
          sg.Text(str(o.payment_method.payment_type), pad=(5, 5), size=(45, 1))  # Valor do obj.
        ])
      Col.append([sg.HSeparator()])
  # Inicialização da interface.
  layout = []
  layout.append([sg.Text('Mostrando informações', pad=(5, 5), size=(25, 1))])
  layout.append(
    [sg.Column(Col, size=(640, 800), element_justification='c', scrollable=True, vertical_scroll_only=True)])
  layout.append([sg.Button('Sair', size=(15, 1), button_color=('white', 'firebrick3'))])
  window = sg.Window("Mostrando Todoas as vendas e lucro total", layout, element_justification='c', resizable=True, finalize=True,
                     modal=True)
  window.TKroot.minsize(320, 240)
  while True:
    event, values = window.read(close=True)
    if event in ["Exit", sg.WIN_CLOSED, "Sair"]:
      break
  window.close()


def show_properties_not_sold(obj_list: list):
    profits: float = 0.0
    Col: list = []
    for prop in obj_list:
        if prop is not None:
            if prop.sale_made is False:
                # layout da página.
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
                        sg.Text(str(prop.property_code), pad=(5, 5), size=(45, 1))  # Valor do obj.
                    ])
                    Col.append(
                        [
                            sg.Text('Endereço: ', pad=(5, 5), size=(20, 1)),
                            sg.Text(str(prop.address), pad=(5, 5), size=(45, 1))
                        ]
                    )
                    Col.append(
                        [
                            sg.Text('Data de construção:', pad=(5, 5), size=(20, 1)),
                            sg.Text(str(prop.construction_date), pad=(5, 5), size=(45, 1))
                        ]
                    )
                    Col.append(
                        [
                            sg.Text('Área total:', pad=(5, 5), size=(20, 1)),
                            sg.Text(str(prop.total_area), pad=(5, 5), size=(45, 1))
                        ]
                    )
                    Col.append(
                        [
                            sg.Text('Área de construção:', pad=(5, 5), size=(20, 1)),
                            sg.Text(str(prop.constructed_area), pad=(5, 5), size=(45, 1))
                        ]
                    )
                    Col.append(
                        [
                            sg.Text('Num. de quartos:', pad=(5, 5), size=(20, 1)),
                            sg.Text(str(prop.num_rooms), pad=(5, 5), size=(45, 1))
                        ]
                    )
                    Col.append(
                        [
                            sg.Text('Num. de banheiros:', pad=(5, 5), size=(20, 1)),
                            sg.Text(str(prop.num_bathrooms), pad=(5, 5), size=(45, 1))
                        ]
                    )
                    Col.append(
                        [
                            sg.Text('Num. de vagas:', pad=(5, 5), size=(20, 1)),
                            sg.Text(str(prop.num_spots_garage), pad=(5, 5), size=(45, 1))
                        ]
                    )
                    Col.append(
                        [
                            sg.Text('IPTU:', pad=(5, 5), size=(20, 1)),
                            sg.Text(str(prop.iptu), pad=(5, 5), size=(45, 1))
                        ]
                    )
                    Col.append(
                        [
                            sg.Text('Valor propriedade:', pad=(5, 5), size=(20, 1)),
                            sg.Text(str(prop.property_worth), pad=(5, 5), size=(45, 1))
                        ]
                    )
                    Col.append(
                        [
                            sg.Text('Valor de aluguel:', pad=(5, 5), size=(20, 1)),
                            sg.Text(str(prop.property_rent), pad=(5, 5), size=(45, 1))
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
                                sg.Text(str(prop.apartment_value), pad=(5, 5), size=(45, 1))
                            ]
                        )
                        Col.append(
                            [
                                sg.Text('Valor do ap:', pad=(5, 5), size=(20, 1)),
                                sg.Text(str(prop.apartment_value), pad=(5, 5), size=(45, 1))
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
                                sg.Text(str(prop.federal_tax), pad=(5, 5), size=(45, 1))
                            ]
                        )
    # Inicialização da interface.
    layout = []
    layout.append([sg.Text('Mostrando informações', pad=(5, 5), size=(25, 1))])
    layout.append(
        [sg.Column(Col, size=(640, 800), element_justification='c', scrollable=True, vertical_scroll_only=True)])
    layout.append([sg.Button('Sair', size=(15, 1), button_color=('white', 'firebrick3'))])
    window = sg.Window("Mostrando todas os imóveis não vendidos", layout, element_justification='c', resizable=True,
                       finalize=True,
                       modal=True)
    window.TKroot.minsize(320, 240)
    while True:
        event, values = window.read(close=True)
        if event in ["Exit", sg.WIN_CLOSED, "Sair"]:
            break
    window.close()


def show_all_sales_and_profit_month_only(obj_list: list, date: str) -> True:
  profits: float = 0.0
  Col: list = []
  for o in obj_list:
    if o is not None:
      if o.sale_date[3:] == date:
        o.print_info()
        # layout da página.
        Col.append([sg.HSeparator()])
        Col.append([
          sg.Text('ID:', pad=(5, 5), size=(20, 1)),  # Label
          sg.Text(str(o.sale_code), pad=(5, 5), size=(45, 1))  # Valor do obj.
        ])
        Col.append([
          sg.Text('Cliente:', pad=(5, 5), size=(20, 1)),  # Label
          sg.Text(str(o.client.name), pad=(5, 5), size=(45, 1))  # Valor do obj.
        ])
        Col.append([
          sg.Text('Corretor:', pad=(5, 5), size=(20, 1)),  # Label
          sg.Text(str(o.broker.name), pad=(5, 5), size=(45, 1))  # Valor do obj.
        ])
        Col.append([
          sg.Text('Imóvel:', pad=(5, 5), size=(20, 1)),  # Label
          sg.Text(str(o.sale_property.address), pad=(5, 5), size=(45, 1))  # Valor do obj.
        ])
        Col.append([
          sg.Text('Data da venda:', pad=(5, 5), size=(20, 1)),  # Label
          sg.Text(str(o.sale_date), pad=(5, 5), size=(45, 1))  # Valor do obj.
        ])
        Col.append([
          sg.Text('Preço da venda:', pad=(5, 5), size=(20, 1)),  # Label
          sg.Text(str(o.total_sale_value), pad=(5, 5), size=(45, 1))  # Valor do obj.
        ])
        Col.append([
          sg.Text('Forma de pagamento:', pad=(5, 5), size=(20, 1)),  # Label
          sg.Text(str(o.payment_method.payment_type), pad=(5, 5), size=(45, 1))  # Valor do obj.
        ])
        profits += o.total_sale_value
      Col.append([sg.HSeparator()])
  Col.append([sg.HSeparator()])
  Col.append([
    sg.Text('Lucro total:', pad=(5, 5), size=(20, 1)),  # Label
    sg.Text(str(profits), pad=(5, 5), size=(45, 1))  # Valor do obj.
  ])
  Col.append([sg.HSeparator()])
  # Inicialização da interface.
  layout = []
  layout.append([sg.Text('Mostrando informações', pad=(5, 5), size=(25, 1))])
  layout.append(
    [sg.Column(Col, size=(640, 800), element_justification='c', scrollable=True, vertical_scroll_only=True)])
  layout.append([sg.Button('Sair', size=(15, 1), button_color=('white', 'firebrick3'))])
  window = sg.Window("Mostrando todas as vendas e lucro total", layout, element_justification='c', resizable=True,
                     finalize=True,
                     modal=True)
  window.TKroot.minsize(320, 240)
  while True:
    event, values = window.read(close=True)
    if event in ["Exit", sg.WIN_CLOSED, "Sair"]:
      break
  window.close()


def show_all_sales_and_profit_month(obj_list) -> object:
  layout = [
    [sg.Text('Digite um mês válido (mm/aaaa):', pad=(5, 5), size=(40, 1)), sg.InputText(size=(32, 1))],
    [sg.Button('Mostrar', pad=(5, 5), size=(21, 1), button_color=('white', 'green4'))]
  ]
  window = sg.Window("Mostrar vendas e lucro em data", layout, element_justification='c', resizable=True, margins=(5, 5))
  while True:
    event, values = window.read(close=True)
    if values is not None:
      if '' in values:
        result_window('Algum campo está vazio, tente novamente.')
        break
      if event in ["Exit", sg.WIN_CLOSED]:
        break
      if event == "Mostrar":
        show_all_sales_and_profit_month_only(obj_list, str(values[0]))
        break
  window.close()


def show_all_sales_by_client(sales_list: list, name: str):
    Col: list = []
    for s in sales_list:
        if s.client.name == name:
            s.print_info()
            # layout da página.
            Col.append([sg.HSeparator()])
            Col.append([
                sg.Text('ID:', pad=(5, 5), size=(20, 1)),  # Label
                sg.Text(str(s.sale_code), pad=(5, 5), size=(45, 1))  # Valor do obj.
            ])
            Col.append([
                sg.Text('Cliente:', pad=(5, 5), size=(20, 1)),  # Label
                sg.Text(str(s.client.name), pad=(5, 5), size=(45, 1))  # Valor do obj.
            ])
            Col.append([
                sg.Text('Corretor:', pad=(5, 5), size=(20, 1)),  # Label
                sg.Text(str(s.broker.name), pad=(5, 5), size=(45, 1))  # Valor do obj.
            ])
            Col.append([
                sg.Text('Imóvel:', pad=(5, 5), size=(20, 1)),  # Label
                sg.Text(str(s.sale_property.address), pad=(5, 5), size=(45, 1))  # Valor do obj.
            ])
            Col.append([
                sg.Text('Data da venda:', pad=(5, 5), size=(20, 1)),  # Label
                sg.Text(str(s.sale_date), pad=(5, 5), size=(45, 1))  # Valor do obj.
            ])
            Col.append([
                sg.Text('Preço da venda:', pad=(5, 5), size=(20, 1)),  # Label
                sg.Text(str(s.total_sale_value), pad=(5, 5), size=(45, 1))  # Valor do obj.
            ])
            Col.append([
                sg.Text('Forma de pagamento:', pad=(5, 5), size=(20, 1)),  # Label
                sg.Text(str(s.payment_method.payment_type), pad=(5, 5), size=(45, 1))  # Valor do obj.
            ])
        Col.append([sg.HSeparator()])
    # Inicialização da interface.
    layout = []
    layout.append([sg.Text('Mostrando informações', pad=(5, 5), size=(25, 1))])
    layout.append(
        [sg.Column(Col, size=(640, 800), element_justification='c', scrollable=True, vertical_scroll_only=True)])
    layout.append([sg.Button('Sair', size=(15, 1), button_color=('white', 'firebrick3'))])
    window = sg.Window("Mostrando todas as vendas e lucro total", layout, element_justification='c', resizable=True,
                       finalize=True,
                       modal=True)
    window.TKroot.minsize(320, 240)
    while True:
        event, values = window.read(close=True)
        if event in ["Exit", sg.WIN_CLOSED, "Sair"]:
            break
    window.close()


def show_properties_sold_to_client(sales_list: list):
  layout = [
    [sg.Text('Digite nome de um cliente:', pad=(5, 5), size=(20, 1)), sg.InputText(size=(32, 1))],
    [sg.Button('Mostrar', pad=(5, 5), size=(21, 1), button_color=('white', 'green4'))]
  ]
  window = sg.Window("Mostrar vendas de um cliente", layout, element_justification='c', resizable=True,
                     margins=(5, 5))
  while True:
    event, values = window.read(close=True)
    if values is not None:
      if '' in values:
        result_window('Algum campo está vazio, tente novamente.')
        break
      if event in ["Exit", sg.WIN_CLOSED]:
        break
      if event == "Mostrar":
        show_all_sales_by_client(sales_list, str(values[0]))
        break
  window.close()

def show_all_rentals(rental_list: list):
      Col: list = []
      for r in rental_list:
          # layout da página.
          Col.append([sg.HSeparator()])
          Col.append([
              sg.Text('ID:', pad=(5, 5), size=(20, 1)),  # Label
              sg.Text(str(r.rent_code), pad=(5, 5), size=(45, 1))  # Valor do obj.
          ])
          Col.append([
              sg.Text('Cliente:', pad=(5, 5), size=(20, 1)),  # Label
              sg.Text(str(r.client.name), pad=(5, 5), size=(45, 1))  # Valor do obj.
          ])
          Col.append([
              sg.Text('Corretor:', pad=(5, 5), size=(20, 1)),  # Label
              sg.Text(str(r.broker.name), pad=(5, 5), size=(45, 1))  # Valor do obj.
          ])
          Col.append([
              sg.Text('Imóvel:', pad=(5, 5), size=(20, 1)),  # Label
              sg.Text(str(r.prop.address), pad=(5, 5), size=(45, 1))  # Valor do obj.
          ])
          Col.append([
              sg.Text('Data de início:', pad=(5, 5), size=(20, 1)),  # Label
              sg.Text(str(r.rent_date), pad=(5, 5), size=(45, 1))  # Valor do obj.
          ])
          Col.append([
              sg.Text('Data de devolução:', pad=(5, 5), size=(20, 1)),  # Label
              sg.Text(str(r.rent_date), pad=(5, 5), size=(45, 1))  # Valor do obj.
          ])
          Col.append([
              sg.Text('Data de pagamento:', pad=(5, 5), size=(20, 1)),  # Label
              sg.Text(str(r.rent_date), pad=(5, 5), size=(45, 1))  # Valor do obj.
          ])
          Col.append([
              sg.Text('Valor do aluguel:', pad=(5, 5), size=(20, 1)),  # Label
              sg.Text(str(r.total_rent_amount), pad=(5, 5), size=(45, 1))  # Valor do obj.
          ])
          Col.append([
              sg.Text('Forma de pagamento:', pad=(5, 5), size=(20, 1)),  # Label
              sg.Text(str(r.payment_method.payment_type), pad=(5, 5), size=(45, 1))  # Valor do obj.
          ])
          for i in r.insurance_hired:
              Col.append([
                  sg.Text('Seguro contratado:', pad=(5, 5), size=(20, 1)),  # Label
                  sg.Text(str(i.insurance_type), pad=(5, 5), size=(45, 1))  # Valor do obj.
              ])
      Col.append([sg.HSeparator()])
      # Inicialização da interface.
      layout = [[sg.Text('Mostrando informações', pad=(5, 5), size=(25, 1))], [
          sg.Column(Col, size=(640, 800), element_justification='c', scrollable=True, vertical_scroll_only=True)],
                [sg.Button('Sair', size=(15, 1), button_color=('white', 'firebrick3'))]]
      window = sg.Window("Mostrando Todos os Alugueis", layout, element_justification='c', resizable=True,
                         finalize=True,
                         modal=True)
      window.TKroot.minsize(320, 240)
      while True:
          event, values = window.read(close=True)
          if event in ["Exit", sg.WIN_CLOSED, "Sair"]:
              break
      window.close()

def show_late_rent(rent_list: list) -> object:
    Col: list = []
    for r in rent_list:
      if r.is_late():
        Col.append([sg.HSeparator()])
        Col.append([
          sg.Text('ID:', pad=(5, 5), size=(20, 1)),  # Label
          sg.Text(str(r.rent_code), pad=(5, 5), size=(45, 1))  # Valor do obj.
        ])
        Col.append([
          sg.Text('Cliente:', pad=(5, 5), size=(20, 1)),  # Label
          sg.Text(str(r.client.name), pad=(5, 5), size=(45, 1))  # Valor do obj.
        ])
        Col.append([
          sg.Text('Corretor:', pad=(5, 5), size=(20, 1)),  # Label
          sg.Text(str(r.broker.name), pad=(5, 5), size=(45, 1))  # Valor do obj.
        ])
        Col.append([
          sg.Text('Imóvel:', pad=(5, 5), size=(20, 1)),  # Label
          sg.Text(str(r.prop.address), pad=(5, 5), size=(45, 1))  # Valor do obj.
        ])
        Col.append([
          sg.Text('Data início da locação:', pad=(5, 5), size=(20, 1)),  # Label
          sg.Text(str(r.rent_date), pad=(5, 5), size=(45, 1))  # Valor do obj.
        ])
        Col.append([
          sg.Text('Data para devolução:', pad=(5, 5), size=(20, 1)),  # Label
          sg.Text(str(r.devolution_date), pad=(5, 5), size=(45, 1))  # Valor do obj.
        ])
        Col.append([
          sg.Text('Data de pagamento:', pad=(5, 5), size=(20, 1)),  # Label
          sg.Text(str(r.payment_date), pad=(5, 5), size=(45, 1))  # Valor do obj.
        ])
        Col.append([
          sg.Text('Total do aluguel:', pad=(5, 5), size=(20, 1)),  # Label
          sg.Text(str(r.total_rent_amount), pad=(5, 5), size=(45, 1))  # Valor do obj.
        ])
        Col.append([
          sg.Text('Pagamento:', pad=(5, 5), size=(20, 1)),  # Label
          sg.Text(str(r.payment_method.payment_type), pad=(5, 5), size=(45, 1))  # Valor do obj.
        ])
        Col.append([
          sg.Text('Quantidade de seguros:', pad=(5, 5), size=(20, 1)),  # Label
          sg.Text(str(len(r.insurance_hired)), pad=(5, 5), size=(45, 1))  # Valor do obj.
        ])
        Col.append([
          sg.Text('Quantidade de seguros:', pad=(5, 5), size=(20, 1)),  # Label
          sg.Text(str(len(r.insurance_hired)), pad=(5, 5), size=(45, 1))  # Valor do obj.
        ])
      Col.append([sg.HSeparator()])

    # Inicialização da interface.
    layout = []
    layout.append([sg.Text('Mostrando informações', pad=(5, 5), size=(25, 1))])
    layout.append(
      [sg.Column(Col, size=(640, 800), element_justification='c', scrollable=True, vertical_scroll_only=True)])
    layout.append([sg.Button('Sair', size=(15, 1), button_color=('white', 'firebrick3'))])
    window = sg.Window("Mostrando os aluguéis atrasados", layout, element_justification='c', resizable=True, finalize=True,
                       modal=True)
    window.TKroot.minsize(320, 240)
    while True:
      event, values = window.read(close=True)
      if event in ["Exit", sg.WIN_CLOSED, "Sair"]:
        break
    window.close()

def show_late_rentals_clients(rental_list: list):
    Col: list = []
    users: list = []
    for r in rental_list:
        if r.is_late:
            users.append(r.client)
    for user in users:
        if user is not None:
            if isinstance(user, UserClient):
                # layout da página.
                Col.append([sg.HSeparator()])
                Col.append([
                    sg.Text('ID:', pad=(5, 5), size=(20, 1)),  # Label
                    sg.Text(str(user.user_code), pad=(5, 5), size=(45, 1))  # Valor do obj.
                ])
                Col.append(
                    [
                        sg.Text('Nome: ', pad=(5, 5), size=(20, 1)),
                        sg.Text(str(user.name), pad=(5, 5), size=(45, 1))
                    ]
                )
                Col.append(
                    [
                        sg.Text('CPF:', pad=(5, 5), size=(20, 1)),
                        sg.Text(str(user.cpf), pad=(5, 5), size=(45, 1))
                    ]
                )
                Col.append(
                    [
                        sg.Text('RG:', pad=(5, 5), size=(20, 1)),
                        sg.Text(str(user.rg), pad=(5, 5), size=(45, 1))
                    ]
                )
                Col.append(
                    [
                        sg.Text('Ano de nascimento:', pad=(5, 5), size=(20, 1)),
                        sg.Text(str(user.anniversary_date), pad=(5, 5), size=(45, 1))
                    ]
                )
                Col.append(
                    [
                        sg.Text('Endereço:', pad=(5, 5), size=(20, 1)),
                        sg.Text(str(user.address), pad=(5, 5), size=(45, 1))
                    ]
                )
                Col.append(
                    [
                        sg.Text('CEP:', pad=(5, 5), size=(20, 1)),
                        sg.Text(str(user.cep), pad=(5, 5), size=(45, 1))
                    ]
                )
                Col.append(
                    [
                        sg.Text('Telefone:', pad=(5, 5), size=(20, 1)),
                        sg.Text(str(user.phone), pad=(5, 5), size=(45, 1))
                    ]
                )
                Col.append(
                    [
                        sg.Text('Email:', pad=(5, 5), size=(20, 1)),
                        sg.Text(str(user.email), pad=(5, 5), size=(45, 1))
                    ]
                )
                Col.append(
                    [
                        sg.Text('Data de registro:', pad=(5, 5), size=(20, 1)),
                        sg.Text(str(user.register_date), pad=(5, 5), size=(45, 1))
                    ]
                )
                Col.append([sg.HSeparator()])
    layout = [[sg.Text('Mostrando informações', pad=(5, 5), size=(25, 1))],
              [sg.Column(Col, size=(640, 800), element_justification='c', scrollable=True, vertical_scroll_only=True)],
              [sg.Button('Sair', size=(15, 1), button_color=('white', 'firebrick3'))]]
    window = sg.Window("Mostrando Clientes em atraso", layout, element_justification='c', resizable=True, finalize=True,
                       modal=True)
    window.TKroot.minsize(320, 240)
    while True:
        event, values = window.read(close=True)
        if event in ["Exit", sg.WIN_CLOSED, "Sair"]:
            break
    window.close()


def show_late_rentals_properties(rental_list: list):
    Col: list = []
    properties: list = []
    for r in rental_list:
        if r.is_late:
            properties.append(r.prop)

    for p in properties:
        Col.append([sg.HSeparator()])
        Col.append([
            sg.Text('ID:', pad=(5, 5), size=(20, 1)),  # Label
            sg.Text(str(p.property_code), pad=(5, 5), size=(45, 1))  # Valor do obj.
        ])
        Col.append([
            sg.Text('Endereço:', pad=(5, 5), size=(20, 1)),  # Label
            sg.Text(str(p.address), pad=(5, 5), size=(45, 1))  # Valor do obj.
        ])
        layout = [[sg.Text('Mostrando informações', pad=(5, 5), size=(25, 1))], [
            sg.Column(Col, size=(640, 800), element_justification='c', scrollable=True, vertical_scroll_only=True)],
                  [sg.Button('Sair', size=(15, 1), button_color=('white', 'firebrick3'))]]
        window = sg.Window("Mostrando imóveis com aluguel em atraso", layout, element_justification='c', resizable=True,
                           finalize=True,
                           modal=True)
        window.TKroot.minsize(320, 240)
        while True:
            event, values = window.read(close=True)
            if event in ["Exit", sg.WIN_CLOSED, "Sair"]:
                break
        window.close()


def show_rentals_by_client(rental_list: list, client: UserClient):
    Col: list = []
    properties: list = []
    for r in rental_list:
        if r.client.client_code == client.user_code:
            properties.append(r.prop)

    for p in properties:
        Col.append([sg.HSeparator()])
        Col.append([
            sg.Text('ID:', pad=(5, 5), size=(20, 1)),  # Label
            sg.Text(str(p.property_code), pad=(5, 5), size=(45, 1))  # Valor do obj.
        ])
        Col.append([
            sg.Text('Endereço:', pad=(5, 5), size=(20, 1)),  # Label
            sg.Text(str(p.address), pad=(5, 5), size=(45, 1))  # Valor do obj.
        ])
        layout = [[sg.Text('Mostrando informações', pad=(5, 5), size=(25, 1))], [
            sg.Column(Col, size=(640, 800), element_justification='c', scrollable=True, vertical_scroll_only=True)],
                  [sg.Button('Sair', size=(15, 1), button_color=('white', 'firebrick3'))]]
        window = sg.Window("Mostrando imóveis alugados por cliente", layout, element_justification='c', resizable=True,
                           finalize=True,
                           modal=True)
        window.TKroot.minsize(320, 240)
        while True:
            event, values = window.read(close=True)
            if event in ["Exit", sg.WIN_CLOSED, "Sair"]:
                break
        window.close()


def show_ative_rentals(rental_list: list):
    ative_rentals: list = []
    for r in rental_list:
        if r.devolution_date >= datetime.now():
            ative_rentals.append(r)
    show_all_rentals(ative_rentals)

def show_ative_home_rentals(rental_list: list):
    home_rentals: list = []
    for r in rental_list:
        if isinstance(r.prop, ResidentialHome):
            home_rentals.append(r)

    show_ative_rentals(home_rentals)


def show_ative_apartment_rentals(rental_list: list):
    apartment_rentals: list = []
    for r in rental_list:
        if isinstance(r.prop, ResidentialApartment):
            apartment_rentals.append(r)

    show_ative_rentals(apartment_rentals)


def show_ative_comercial_rentals(rental_list: list):
    comercial_rentals: list = []
    for r in rental_list:
        if isinstance(r.prop, Comercial):
            comercial_rentals.append(r)

    show_ative_rentals(comercial_rentals)

def show_inative_rentals(rental_list: list):
    inative_rentals: list = []
    for r in rental_list:
        if r.devolution_date < datetime.now():
            inative_rentals.append(r)
    show_all_rentals(inative_rentals)

# FIM Mostrar Objetos
