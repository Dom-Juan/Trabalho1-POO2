import json
import sys
import datetime

from datetime import date
from os import path

import PySimpleGUI as sg

sys.path.append('..\\..')
from classes.user.user import User


class UserBroker(User):
  def __init__(self, name: str, cpf: str, rg: str, anniversary_date: str, address: str, cep: str, phone: str,
               email: str, growf: str, wage: float, pis: str, hired_date: str):
    super(UserBroker, self).__init__(name, cpf, rg, anniversary_date, address, cep, phone, email)
    self._growf: str = growf
    self._wage: float = wage
    self._pis: str = pis
    self._hired_date: str = hired_date

  @property
  def growf(self):
    return self._growf

  @growf.setter
  def growf(self, value):
    self._growf = value
    pass

  @property
  def wage(self):
    return self._wage

  @wage.setter
  def wage(self, value):
    self._wage = value
    pass

  @property
  def pis(self):
    return self._pis

  @pis.setter
  def pis(self, value):
    self._pis = value
    pass

  @property
  def hired_date(self):
    return self._hired_date

  @hired_date.setter
  def hired_date(self, value):
    self._hired_date = value
    pass

  @property
  def user_code(self):
    return self._user_code

  @user_code.setter
  def user_code(self, value):
    self._user_code = value
    pass

  @property
  def name(self):
    return self._name

  @name.setter
  def name(self, value):
    self._name = value
    pass

  @property
  def cpf(self):
    return self._cpf

  @cpf.setter
  def cpf(self, value):
    self._cpf = value
    pass

  @property
  def rg(self):
    return self._rg

  @rg.setter
  def rg(self, value):
    self._rg = value
    pass

  @property
  def anniversary_date(self):
    return self._anniversary_date

  @anniversary_date.setter
  def anniversary_date(self, value):
    self._anniversary_date = value
    pass

  @property
  def address(self):
    return self._address

  @address.setter
  def address(self, value):
    self._address = value
    pass

  @property
  def cep(self):
    return self._cep

  @cep.setter
  def cep(self, value):
    self._cep = value
    pass

  @property
  def phone(self):
    return self._phone

  @phone.setter
  def phone(self, value):
    self._phone = value
    pass

  @property
  def email(self):
    return self._email

  @email.setter
  def email(self, value):
    self._email = value
    pass

  def print_obj(self):
    self._layout = [
      [sg.Text(self.hired_date)],
      [sg.Text(self.user_code)],
      [sg.Text(self.name)],
      [sg.Text(self.cpf)],
      [sg.Text(self.rg)],
      [sg.Text(self.anniversary_date)],
      [sg.Text(self.address)],
      [sg.Text(self.cep)],
      [sg.Text(self.phone)],
      [sg.Text(self.email)],
      [sg.Text(self.growf)],
      [sg.Text(self.wage)],
      [sg.Text(self.pis)],
      [sg.Text(self.hired_date)],
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
      if item['user_code']  == self.user_code:
        print("usuario já existe")
        listObj.remove(item)
    print(type(listObj))
    listObj.append({
      "type": "broker",
      "user_code": self.user_code,
      "name": self.name,
      "cpf": self.cpf,
      "rg": self.rg,
      "anniversary_date": self.anniversary_date,
      "address": self.address,
      "cep": self.cep,
      "phone": self.phone,
      "email": self.email,
      "hired_date": self.hired_date,
      "growf": self.growf,
      "wage": self.wage,
      "pis": self.pis,
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
