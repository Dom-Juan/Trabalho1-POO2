import random
import datetime

class User():
  def __init__(self, name: str, cpf: str, rg: str, anniversary_date: str, address: str, cep: str, phone: str,
               email: str):
    self._user_code: int = random.randint(0, 9999)
    self._name: str = name
    self._cpf: str = cpf
    self._rg: str = rg
    if anniversary_date == (None or ''):
      self._anniversary_date: any = None
    else:
      self._anniversary_date: str = datetime.datetime.strptime(anniversary_date, '%d/%m/%Y').date().strftime('%d/%m/%Y')
    self._address: str = address
    self._cep: str = cep
    self._phone: str = phone
    self._email: str = email
    self._layout = []

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
    pass