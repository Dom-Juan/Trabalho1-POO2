import random
import datetime

from abc import ABC, abstractmethod

class User(ABC):
  def __init__(self, name: str, cpf: str, rg: str, anniversary_date: str, address: str, cep: str, phone: str,
               email: str):
    self._user_code: int = random.randint(0, 9999)
    self._name: str = name,
    self._cpf: str = cpf
    self._rg: str = rg
    self._anniversary_date: str = datetime.datetime.strptime(anniversary_date, '%d/%m/%Y').date().strftime('%d/%m/%Y')
    self._address: str = address,
    self._cep: str = cep,
    self._phone: str = phone,
    self._email: str = email,
    self._layout = []

  @abstractmethod
  def get_user_code(self):
    pass

  @abstractmethod
  def set_user_code(self, value: int):
    pass

  @abstractmethod
  def get_name(self):
    pass

  @abstractmethod
  def set_name(self, value):
    pass

  @abstractmethod
  def get_cpf(self):
    pass

  @abstractmethod
  def set_cpf(self, value):
    pass

  @abstractmethod
  def get_rg(self):
    pass

  @abstractmethod
  def set_rg(self, value):
    pass

  @abstractmethod
  def get_anniversary_date(self):
    pass

  @abstractmethod
  def set_anniversary_date(self, value):
    pass

  @abstractmethod
  def get_address(self):
    pass

  @abstractmethod
  def set_address(self, value):
    pass

  @abstractmethod
  def get_cep(self):
    pass

  @abstractmethod
  def set_cep(self, value):
    pass

  @abstractmethod
  def get_phone(self):
    pass

  @abstractmethod
  def set_phone(self, value):
    pass

  @abstractmethod
  def get_email(self):
    pass

  @abstractmethod
  def set_email(self, value):
    pass

  @abstractmethod
  def print_obj(self):
    pass