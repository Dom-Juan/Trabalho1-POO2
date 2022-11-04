import json

from os import path
from classes.money.payment import Payment


class PaymentByMoney(Payment):
  def __init__(self, payment_type: str, total_charge: float):
    super().__init__(payment_type)
    self._total_charge = total_charge
    pass

  @property
  def total_charge(self):
    return self._total_charge

  @total_charge.setter
  def total_charge(self, value):
    self._total_charge = value
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
      "type": "payment_money",
      "payment_code": self.payment_code,
      "payment_type:": self.payment_type,
      "total_charge": self.total_charge,
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