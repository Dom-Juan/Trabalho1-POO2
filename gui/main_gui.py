import PySimpleGUI as sg
import sys
import pyglet

from gui.gui_create_obj import create_client, create_broker, create_comercial, create_apartment, create_house, \
  create_insurance, create_payment_method_card, create_payment_method_money, create_sale
from gui.gui_load_obj import load_file_gui_insurance, load_file_gui_property, load_file_gui_users
from gui.gui_show_obj import show_all_insurance, show_ap_property, show_comercial_property,\
  show_home_property, show_all_property, show_users_broker, show_users_client

# import de classes
sys.path.append('../')
from classes.real_state_company.real_state_company import RealStateCompany


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
def main_window(name, real_state_company_name):
  # Instanciando a imobiliária
  user_list: list = list()
  property_list: list = list()
  insurance_list: list = list()
  payment_list: list = list()
  rental_list: list = list()
  sale_list: list = list()
  real_state_company = RealStateCompany(
    real_state_company_name, "Rua Abacate Felicidade",
    rental_list, sale_list,
    property_list,
    user_list,
    insurance_list,
    []
  )
  pyglet.font.add_file(r"./fonts/Roboto-Regular.ttf")
  font1 = ("Roboto Regular", 12)
  sg.set_options(font=font1)
  sg.theme('SystemDefault')
  Col = [
    [
      sg.HSeparator()
    ],
    [
      sg.Text('Operações Pedidas no PDF.')
    ],
    [
      sg.Button('Mostar todos Imóveis', size=(25, 2), key='-ALLPROPERTY-'),
    ],
    [
      sg.HSeparator()
    ],
    [
      sg.Button('Sair', size=(15, 1), button_color=('white', 'firebrick3'))
    ]
  ]
  layout = []
  layout.append(
    [
      sg.Menu(
        [
          [
            '&Usuários',
              [
                'Criar Cliente',
                'Criar Corretor',
                'Mostrar todos Clientes',
                'Mostar todos Corretores',
                'Salvar arquivo usuários',
                'Carregar arquivo usuários'
              ],
          ],
          [
            '&Imóveis',
            [
              'Criar Apartamento',
              'Criar Casa',
              'Criar Comercio',
              'Mostar todos as Casas',
              'Mostar todos os Apartamentos',
              'Mostar todos os Comércios',
              'Salvar arquivo imoveis',
              'Carregar arquivo imoveis'
            ]
          ],
          [
            '&Seguro',
            [
              'Criar Seguro',
              'Mostar Seguros',
              'Salvar arquivo do seguro',
              'Carregar arquivo do seguro'
            ]
          ],
          [
            '&Métodos de Pagamentos',
            [
              'Criar Pagamento Dinheiro',
              'Criar Pagamento Cartão',
              'Mostar todos pagamentos com Dinheiro',
              'Mostar todos pagamentos com Cartão',
              'Carregar arquivo pagamento',
              'Salvar arquivo pagamento'
            ]
          ],
          [
            '&Alugéis',
            [
              'Criar Aluguel',
              'Mostar todos os alugueis',
              'Salvar arquivo aluguel',
              'Carregar arquivo aluguel'
            ]
          ],
          [
            '&Vendas',
            [
              'Criar Venda',
              'Mostar todos as vendas',
              'Salvar arquivo venda',
              'Carregar arquivo venda'
            ]
          ],
          [
            '&Imobiliária',
            [
              'Salvar arquivo da imobiliaria'
            ]
          ],
        ],
        font=('Cascadia Code', 12),
        tearoff=False,
        pad=(200, 5),
      )
    ]
  )
  layout.append(
    [
      sg.Column(Col, scrollable=True,  justification="right", pad=(0, 0), size=(1280, 720))
    ]
  )
  layout2 = []  # layout da janela
  # Configurações da página.
  window = sg.Window(name, layout, size=(1280, 720), resizable=True, enable_close_attempted_event=True, finalize=True)
  # Objetos instanciados com Null para receberem os ponteiros depois.
  obj: object = None
  while True:
    event, values = window.read()
    layout2.append([sg.Text('Resultado'), values])

    print(event)

    if event in [sg.WIN_CLOSE_ATTEMPTED_EVENT, 'Sair']:
      break
    if event == "Botão da Sara":
      janela = 1 # colocar a função da janela em que sera editada.
    # Lógica de criação dos objetos.
    if event == "Criar Cliente":
      obj = create_client()
      print(f"Main loop, ", obj)
      if obj is not None:
        real_state_company.add_user(obj)
    if event == "Criar Corretor":
      obj = create_broker()
      print(f"Main loop, ", obj)
      if obj is not None:
        real_state_company.add_user(obj)
    if event == "Criar Casa":
      obj = create_house()
      print(f"Main loop, ", obj)
      if obj is not None:
        real_state_company.add_real_state_properties(obj)
    if event == "Criar Apartamento":
      obj = create_apartment()
      print(f"Main loop, ", obj)
      if obj is not None:
        real_state_company.add_real_state_properties(obj)
    if event == "Criar Comercio":
      obj = create_comercial()
      print(f"Main loop, ", obj)
      if obj is not None:
        real_state_company.add_real_state_properties(obj)
    if event == "Criar Seguro":
      obj = create_insurance()
      if obj is not None:
        real_state_company.add_insurance(obj)
    if event == "Criar Pagamento Dinheiro":
      obj = create_payment_method_money()
      if obj is not None:
        payment_list.append(obj)
    if event == "Criar Pagamento Cartão":
      obj = create_payment_method_card()
      if obj is not None:
        payment_list.append(obj)
    if event == "Criar Venda":
      obj = create_sale(real_state_company.users, real_state_company.real_state_properties, payment_list)
      if obj is not None:
        real_state_company.add_sales(obj)
    # Lógica de mostrar info dos objetos.
    if event == "Mostrar todos Clientes":
      show_users_client(real_state_company.users)
    if event == "Mostar todos Corretores":
      show_users_broker(real_state_company.users)
    if event in ['Mostar todos os Imóveis', '-ALLPROPERTY-']:
      show_all_property(real_state_company.real_state_properties)
    if event == 'Mostar todos as Casas':
      show_home_property(real_state_company.real_state_properties)
    if event in ['Mostar todos os Apartamentos', '-ALLPROPERTYAPARTMENT-']:
      show_ap_property(real_state_company.real_state_properties)
    if event in ['Mostar todos os Comércios', '-ALLPROPERTYCOMERCIAL-']:
      show_comercial_property(real_state_company.real_state_properties)
    if event == "Mostar Seguros":
      show_all_insurance(real_state_company.insurance)
    # Lógicas de carregar arquivos.
    if event == "Carregar arquivo usuários":
      new_user_list: list = load_file_gui_users()
      if new_user_list != None:
        for u in new_user_list[:]:
          real_state_company.add_user(u)
        result_window('Arquivo carregado com sucesso!')
    if event == 'Carregar arquivo imoveis':
      new_property_list: list = load_file_gui_property()
      if new_property_list != None:
        for p in new_property_list[:]:
          real_state_company.add_real_state_properties(p)
        result_window('Arquivo carregado com sucesso!')
    if event in ['Carregar arquivo do seguro', '-LOADALLINSURANCE-']:
      new_insurance_list: list = load_file_gui_insurance()
      if new_insurance_list != None:
        for i in new_insurance_list[:]:
          real_state_company.add_insurance(i)
        result_window('Arquivo carregado com sucesso!')
    # Lógicas de salvar arquivos.
    if event == "Salvar arquivo usuários":
      for u in real_state_company.users:
        u.save_json_file()
      result_window('Arquivo salvo com sucesso!')
    if event in ["Salvar arquivo imoveis", '-SAVEALLPROPERTY-']:
      for p in real_state_company.real_state_properties:
        p.save_json_file()
      result_window('Arquivo salvo com sucesso!')
    if event in ["Salvar arquivo do seguro", '-SAVEALLINSURANCE-']:
      for i in real_state_company.insurance:
        i.save_json_file()
      result_window('Arquivo salvo com sucesso!')
    if event in ['Salvar arquivo da imobiliaria', '-SAVEALREALSTATECOMPANY-']:
      real_state_company.save_json_file()
      result_window('Arquivo salvo com sucesso!')
    obj = None
  window.close()