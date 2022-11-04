import json
import sys
import datetime

from datetime import date
from os import path

sys.path.append('../')
sys.path.append('../')
from classes.property.property import Property


class Comercial(Property):
  def __init__(
      self,
      address: str,
      construction_date: str,
      total_area: float,
      constructed_area: float,
      num_rooms: int,
      num_bathrooms: int,
      num_spots_garage: int,
      iptu: float,
      property_worth: float,
      property_rent: float,
      federal_tax: float
  ):
    super().__init__(
      address,
      construction_date,
      total_area,
      constructed_area,
      num_rooms,
      num_bathrooms,
      num_spots_garage,
      iptu,
      property_worth,
      property_rent
    )
    self._federal_tax = federal_tax

  @property
  def federal_tax(self):
    return self.federal_tax

  @federal_tax.setter
  def federal_tax(self, value):
    self._federal_tax = value
    pass

  def rent_value(self):
    self.property_rent = (self.property_worth * 0.45) + self.federal_tax
    return self.property_rent

  def save_json_file(self) -> str:
    filename = './files/property_data.json'
    if path.isfile(filename) is False:
      return "> File not found"
      raise Exception("File not found")
    # Lendo o arquivo json
    with open(filename) as fp:
      listObj = json.load(fp)
    print(listObj)
    for item in listObj:
      if item['property_code'] == self.property_code:
        print("propriedade já existe!")
        listObj.remove(item)
    print(type(listObj))
    listObj.append({
      "type": "comercial",
      "property_code": self.property_code,
      "address": self.address,
      "construction_date": self.construction_date,
      "total_area": self.total_area,
      "constructed_area": self.constructed_area,
      "num_rooms": self.num_rooms,
      "num_bathrooms": self.num_bathrooms,
      "num_spots_garage": self.num_spots_garage,
      "iptu": self.iptu,
      "property_worth": self.property_worth,
      "property_rent": self.property_rent,
      "federal_tax": self.federal_tax
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
