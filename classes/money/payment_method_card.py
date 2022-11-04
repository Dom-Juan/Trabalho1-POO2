import json

from os import path
from classes.money.payment import Payment


class PaymentByCard(Payment):
  def __init__(self, payment_type: str, card_name: str, flag: str, number: str):
    super().__init__(payment_type)
    self._card_name: str = card_name
    self._flag: str = flag
    self._number: str = number
    pass

  @property
  def card_name(self):
    return self._card_name

  @card_name.setter
  def card_name(self, value):
    self._card_name = value
    pass

  @property
  def flag(self):
    return self._flag

  @flag.setter
  def flag(self, value):
    self._flag = value
    pass

  @property
  def number(self):
    return self._number

  @number.setter
  def number(self, value):
    self.number = value
    pass

  def save_json_file(self) -> str:
    filename = './files/payment_data.json'
    if path.isfile(filename) is False:
      return "> File not found"
      raise Exception("File not found")
    # Lendo o arquivo json
    with open(filename) as fp:
      listObj = json.load(fp)
    print(listObj)
    for item in listObj:
      if item['payment_code'] == self.payment_code:
        print("método já existe já existe!")
        listObj.remove(item)
    print(type(listObj))
    listObj.append({
      "type": "payment_card",
      "payment_code": self.payment_code,
      "payment_type:": self.payment_type,
      "card_name": self.card_name,
      "flag": self.flag,
      "number": self.number,
    })
    # Verificando JSON atualizado
    print(listObj)
    # Escrevendo JSON
    with open(filename, 'w', encoding='utf-8') as json_file:
      json.dump(listObj, json_file,
                indent=4,
                separators=(',', ': '),
                ensure_ascii=True)
    return "> Arquivo JSON atualizado com sucesso!"