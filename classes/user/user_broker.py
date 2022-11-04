import json
import sys
import datetime

from abc import ABC
from datetime import date
from os import path

import PySimpleGUI as sg

sys.path.append('../')
sys.path.append('../')
from classes.user.user import User


class UserBroker(User, ABC):
  def __init__(self, name: str, cpf: str, rg: str, anniversary_date: str, address: str, cep: str, phone: str,
               email: str, growf: str, wage: float, pis: str, hired_date: str):
    super(UserBroker, self).__init__(name, cpf, rg, anniversary_date, address, cep, phone, email)
    self._growf: str = growf
    self._wage: float = wage
    self._pis: str = pis
    self._hired_date: str = hired_date

  def get_growf(self):
    return self._growf

  def set_growf(self, value: str):
    self._growf = value
    pass

  def get_wage(self):
    return self._wage

  def set_wage(self, value: float):
    self._wage = value
    pass

  def get_pis(self):
    return self._pis

  def set_pis(self, value: str):
    self._pis = value
    pass

  def get_hired_date(self):
    return self._hired_date

  def set_hired_date(self, value: str):
    self._hired_date: str = value
    pass

  def get_user_code(self):
    return self._user_code

  def set_user_code(self, value: int):
    self._user_code = value
    pass

  def get_name(self):
    return self._name

  def set_name(self, value):
    self._name = value
    pass

  def get_cpf(self):
    return self._cpf

  def set_cpf(self, value):
    self._cpf = value
    pass

  def get_rg(self):
    return self._rg

  def set_rg(self, value):
    self._rg = value
    pass

  def get_anniversary_date(self):
    return self._anniversary_date

  def set_anniversary_date(self, value):
    self._anniversary_date = datetime.strptime(value, '%d/%m/%Y').date().strftime('%d/%m/%Y')
    pass

  def get_address(self):
    return self._address

  def set_address(self, value):
    self._address = value
    pass

  def get_cep(self):
    return self._cep

  def set_cep(self, value):
    self._cep = value
    pass

  def get_phone(self):
    return self._phone

  def set_phone(self, value):
    self._phone = value
    pass

  def get_email(self):
    return self._email

  def set_email(self, value):
    self._email = value

  def print_obj(self):
    self._layout = [
      [sg.Text(self._hired_date)],
      [sg.Text(self._user_code)],
      [sg.Text(self._name)],
      [sg.Text(self._cpf)],
      [sg.Text(self._rg)],
      [sg.Text(self._anniversary_date)],
      [sg.Text(self._address)],
      [sg.Text(self._cep)],
      [sg.Text(self._phone)],
      [sg.Text(self._email)],
      [sg.Text(self._growf)],
      [sg.Text(self._wage)],
      [sg.Text(self._pis)],
      [sg.Text(self._hired_date)],
      [sg.Button('Ok')]
    ]
    window = sg.Window("Print do Cliente.", self._layout, size=(640, 480), resizable=True, modal=True)
    while True:
      event, values = window.read()
      if event in ["Exit", sg.WIN_CLOSED, "Ok"]:
        break
    window.close()
    pass

  def save_json_file(self):
    filename = './files/user_data.json'
    if path.isfile(filename) is False:
      raise Exception("File not found")
    # Lendo o arquivo json
    with open(filename) as fp:
      listObj = json.load(fp)
    print(listObj)
    for item in listObj:
      if item['user_code']  == self.get_user_code():
        print("usuario já existe")
        listObj.remove(item)
    print(type(listObj))
    listObj.append({
      "type": "broker",
      "user_code": self._user_code,
      "name": self._name,
      "cpf": self._cpf,
      "rg": self._rg,
      "anniversary_date": self._anniversary_date,
      "address": self._address,
      "cep": self._cep,
      "phone": self._phone,
      "email": self._email,
      "hired_date": self._hired_date,
      "growf": self._growf,
      "wage": self._wage,
      "pis": self._pis,
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
