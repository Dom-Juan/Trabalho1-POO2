import PySimpleGUI as sg
import sys

from gui.gui_create_obj import create_client, create_broker, create_comercial, create_apartment, create_house
from gui.gui_load_obj import load_file_gui_property, load_file_gui_users
from gui.gui_show_obj import print_info, show_property, show_users, show_all_property

# import de classes
sys.path.append('../')
from classes.user.user_broker import UserBroker


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


# Janela principal.
def main_window(name):
  sg.set_options(font=("Cascadia Code", 12))
  sg.theme('DarkAmber')
  Col = [
    [
      sg.Text('Operações básicas.', justification="center")
    ],
    [
      sg.HSeparator()
    ],
    [
      sg.Text('Registar dados: ', size=(20, 2)),
      sg.Button('Criar Cliente', size=(25, 2)),
      sg.Button('Criar Corretor', size=(25, 2)),
      sg.Button('Criar Apartamento', size=(25, 2)),
      sg.Button('Criar Casa', size=(25, 2)),
      sg.Button('Criar Comercio', size=(25, 2)),
    ],
    [
      sg.Text('Mostrar dados: ', size=(20, 1)),
      sg.Button('Mostrar todos Clientes', size=(25, 2)),
      sg.Button('Mostar todos Corretores', size=(25, 2)),
      sg.Button('Mostar todos Imóveis', size=(25, 2), key='-ALLPROPERTY-'),
      sg.Button('Mostar todas as Casas', size=(25, 2), key='-ALLPROPERTYHOME-'),
      sg.Button('Mostar todos os Apartamentos', size=(25, 2), key='-ALLPROPERTYAPARTMENT-'),
      sg.Button('Mostar todos os Comércios', size=(25, 2), key='-ALLPROPERTYCOMERCIAL-'),
    ],
    [
      sg.Text('Carregar dados: ', size=(20, 2)),
      sg.Button('Carregar arquivo usuários', size=(25, 2)),
      sg.Button('Carregar arquivo imoveis', size=(25, 2)),
      sg.Button('Carregar arquivo pagamento', size=(25, 2)),
      sg.Button('Carregar arquivo seguro', size=(25, 2)),
      sg.Button('Carregar arquivo aluguel', size=(25, 2)),
      sg.Button('Carregar arquivo imob.', size=(25, 2)),
      sg.Button('Carregar arquivo venda', size=(25, 2)),
    ],
    [
      sg.Text('Salvar dados: ', size=(20, 2)),
      sg.Button('Salvar arquivo usuários', size=(25, 2)),
      sg.Button('Salvar arquivo imoveis', size=(25, 2), key='-SAVEALLPROPERTY-'),
      sg.Button('Salvar arquivo pagamento', size=(25, 2)),
      sg.Button('Salvar arquivo seguro', size=(25, 2)),
      sg.Button('Salvar arquivo aluguel', size=(25, 2)),
      sg.Button('Salvar arquivo imob.', size=(25, 2)),
      sg.Button('Salvar arquivo venda', size=(25, 2)),
    ],
    [
      sg.HSeparator()
    ],
    [
      sg.Text('Operações pedidas.')
    ],
    [
      sg.Text('[TODO...]')
    ],
    [
      sg.HSeparator()
    ],
    [
      sg.Button('Sair', size=(15, 1), button_color=('white', 'firebrick3'))
    ]
  ]
  layout = [
    [
      sg.Column(Col, scrollable=True,  justification="right", pad=(0, 0), size=(1280, 720)),
    ]
  ]
  layout2 = []  # layout da janela
  # Configurações da página.
  window = sg.Window(name, layout, size=(1280, 720), resizable=True, margins=(0, 0), finalize=True)
  # Array de objetos instanciados.
  user_list: list = list()
  property_list: list = list()
  # Objetos instanciados com Null para receberem os ponteiros depois.
  obj: object = None
  while True:
    event, values = window.read()
    layout2.append([sg.Text('Resultado'), values])
    if event in [sg.WIN_CLOSED, 'Sair']:
      break
    # Lógica de criação dos objetos.
    if event == "Criar Cliente":
      obj = create_client()
      print(f"Main loop, ", obj)
      user_list.append(obj)
    if event == "Criar Corretor":
      obj = create_broker()
      print(f"Main loop, ", obj)
      user_list.append(obj)
    if event == "Criar Casa":
      obj = create_house()
      print(f"Main loop, ", obj)
      property_list.append(obj)
    if event == "Criar Apartamento":
      obj = create_apartment()
      print(f"Main loop, ", obj)
      property_list.append(obj)
    if event == "Criar Comercio":
      obj = create_comercial()
      print(f"Main loop, ", obj)
      property_list.append(obj)
    # Lógica de mostrar info dos objetos.
    if event == "Mostrar todos Clientes":
      show_users(user_list, "clientes")
    if event == "Mostar todos Corretores":
      print_info(UserBroker, user_list)
    if event in ['Mostar todos os Imóveis', '-ALLPROPERTY-']:
      show_all_property(property_list)
    if event in ['Mostar todos as Casas', '-ALLPROPERTYHOME-']:
      show_property(property_list, "h")
    if event in ['Mostar todos os Apartamentos', '-ALLPROPERTYAPARTMENT-']:
      show_property(property_list, "ap")
    if event in ['Mostar todos os Comércios', '-ALLPROPERTYCOMERCIAL-']:
      show_property(property_list, "c")
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
      result_window('Arquivo salvo com sucesso!')
    if event in ["Salvar arquivo imoveis", '-SAVEALLPROPERTY-']:
      for i in property_list:
        i.save_json_file()
      result_window('Arquivo salvo com sucesso!')
    obj = None
  window.close()