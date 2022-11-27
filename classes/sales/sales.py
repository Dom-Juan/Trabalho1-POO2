import json
import sys
import datetime
import random

from datetime import date
from os import path

import PySimpleGUI as sg

sys.path.append('..\\..')
from classes.user.user_client import UserClient
from classes.user.user_broker import UserBroker
from classes.property.property import Property
from classes.money.payment import Payment


class Sale:
  def __init__(self, client: UserClient, broker: UserBroker, sale_property: Property, 
    sale_date: str, total_sale_value: float, payment_method: Payment):

    self.__sale_code: int = random.randint(0, 9999)
    self.__client: UserCliente = client
    self.__broker: UserBroker = broker
    self.__sale_property: Property = sale_property
    if sale_date == (None or ''):
      self.__sale_date: any = None
    else:
      self.__sale_date: str = datetime.datetime.strptime(sale_date, '%d/%m/%Y').date().strftime('%d/%m/%Y')
    self.__total_sale_value: float = total_sale_value
    self.__payment_method: Payment = payment_method

  @property
  def sale_code(self):
    return self.__sale_code

  @sale_code.setter
  def insurance_code(self, value: int):
    self.__sale_code = value
    pass

  @property
  def client(self):
    return self.__client

  @client.setter
  def client(self, value: UserClient):
    self.__client = value
    pass

  @property
  def broker(self):
    return self.__broker

  @broker.setter
  def broker(self, value: UserBroker):
    self.__broker = value
    pass

  @property
  def sale_property(self):
    return self.__sale_property

  @sale_property.setter
  def sale_property(self, value: Property):
    self.__sale_property = value
    pass

  @property
  def sale_date(self):
    return self.__sale_date

  @sale_date.setter
  def sale_date(self, value: str):
    self.__sale_date = value
    pass

  @property
  def total_sale_value(self):
    return self.__total_sale_value

  @total_sale_value.setter
  def total_sale_value(self, value: float):
    self.__total_sale_value = value
    pass

  @property
  def payment_method(self):
    return self.__payment_method

  @payment_method.setter
  def payment_method(self, value: Payment):
    self.__payment_method = value
    pass

  def print_obj(self):
    self._layout = [
      [sg.Text(self.sale_code)],
      [sg.Text(self.client.name)],
      [sg.Text(self.broker.name)],
      [sg.Text(self.sale_property.address)],
      [sg.Text(self.sale_date)],
      [sg.Text(self.total_sale_value)],
      [sg.Text(self.payment_method.payment_code)],
      [sg.Button('Ok')]
    ]
    window = sg.Window("Print da Venda.", self._layout, size=(640, 480), resizable=True, modal=True)
    while True:
      event, values = window.read()
      if event in ["Exit", sg.WIN_CLOSED, "Ok"]:
        break
    window.close()
    pass

  def save_json_file(self):
    filename = './files/sale_data.json'
    if path.isfile(filename) is False:
      raise Exception("File not found")
    # Lendo o arquivo json
    with open(filename) as fp:
      listObj = json.load(fp)
    print(listObj)
    for item in listObj:
      if item['sale_code'] == self.sale_code:
        print("venda já existe")
        listObj.remove(item)
    print(type(listObj))
    listObj.append({
      "sale_code": self.sale_code,
      "client": self.client.name,
      "broker": self.broker.name,
      "sale_property": self.sale_property.address,
      "sale_date": self.sale_date,
      "total_sale_value": self.total_sale_value,
      "payment_method": self.payment_method.payment_code
    })
    # Verificando JSON atualizado
    print(listObj)
    # Escrevendo JSON
    with open(filename, 'w', encoding='utf-8') as json_file:
      json.dump(listObj, json_file,
                indent=4,
                separators=(',', ': '),
                ensure_ascii=True)
    print('> Arquivo JSON atualizado com sucesso!')
    pass

if __name__ == '__main__':
  from classes.property.residential_apartment import ResidentialApartment
  from classes.money.payment_method_card import PaymentByCard

  print("DEBUG")
  c = UserClient("joão", "a", "a", "06/06/1998", "a", "a", "a", "a")
  b = UserBroker("pedro", "a", "a", "06/06/1999", "a", "a", "a", "a", "a", 123, "a", "a")
  p = ResidentialApartment("rua limão", "a", 123, 123, 111, 111, 111, 123, 123, 123, 111, 123)
  pm = PaymentByCard("cartão", "a", "a", "a")
  u = Sale(c, b, p, "06/06/2009", 40_000, pm)
  u.print_obj()
