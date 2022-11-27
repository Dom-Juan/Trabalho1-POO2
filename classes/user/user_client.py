import json
import sys
import datetime

from datetime import date
from os import path

import PySimpleGUI as sg

sys.path.append('..\\..')
from classes.user.user import User


class UserClient(User):
  def __init__(self, name: str, cpf: str, rg: str, anniversary_date: str, address: str, cep: str, phone: str,
               email: str):
    super(UserClient, self).__init__(name, cpf, rg, anniversary_date, address, cep, phone, email)
    today = date.today()
    self._register_date = today.strftime("%d/%m/%Y")

  @property
  def register_date(self):
    return self._register_date

  @register_date.setter
  def register_date(self, value):
    self._register_date = value
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
    self._anniversary_date = datetime.strptime(value, '%d/%m/%Y').date().strftime('%d/%m/%Y')
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
      [sg.Text(self.register_date)],
      [sg.Text(self.user_code)],
      [sg.Text(self.name)],
      [sg.Text(self.cpf)],
      [sg.Text(self.rg)],
      [sg.Text(self.anniversary_date)],
      [sg.Text(self.address)],
      [sg.Text(self.cep)],
      [sg.Text(self.phone)],
      [sg.Text(self.email)],
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
      if item['user_code'] == self.get_user_code():
        print("usuario já existe")
        listObj.remove(item)
    print(type(listObj))
    listObj.append({
      "type": "client",
      "user_code": self.user_code,
      "name": self.name,
      "cpf": self.cpf,
      "rg": self.rg,
      "anniversary_date": self.anniversary_date,
      "address": self.address,
      "cep": self.cep,
      "phone": self.phone,
      "email": self.email,
      "register_date": self.register_date
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
  print("DEBUG")
  u = UserClient("a", "a", "a", "06/06/1998", "a", "a", "a", "a")
  u.print_obj()