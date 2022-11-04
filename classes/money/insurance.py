import json
import uuid

from os import path

class Insurance:
  def __init__(self, insurance_name: str, insurance_type: str, insurance_desc: str, insurance_value: float):
    self.__insurance_code: int = uuid.uuid1().int
    self.__insurance_name: str = insurance_name
    self.__insurance_type: str = insurance_type
    self.__insurance_desc: str = insurance_desc
    self.__insurance_value: float = insurance_value
    pass

  @property
  def insurance_code(self):
    return self.__insurance_code

  @insurance_code.setter
  def insurance_code(self, value):
    self.__insurance_code = value
    pass
  @property
  def insurance_name(self):
    return self.__insurance_name

  @insurance_name.setter
  def insurance_name(self, value):
    self.__insurance_name = value
    pass

  @property
  def insurance_type(self):
    return self.__insurance_type

  @insurance_type.setter
  def insurance_type(self, value):
    self.__insurance_type = value
    pass

  @property
  def insurance_desc(self):
    return self.__insurance_desc

  @insurance_desc.setter
  def insurance_desc(self, value):
    self.__insurance_desc = value
    pass

  @property
  def insurance_value(self):
    return self.__insurance_value

  @insurance_value.setter
  def insurance_value(self, value):
    self.__insurance_value = value
    pass

  def save_json_file(self) -> str:
    filename = './files/insurance_data.json'
    if path.isfile(filename) is False:
      return "> File not found"
      raise Exception("File not found")
    # Lendo o arquivo json
    with open(filename) as fp:
      listObj = json.load(fp)
    print(listObj)
    for item in listObj:
      if item['insurance_code'] == self.insurance_code:
        print("propriedade já existe!")
        listObj.remove(item)
    print(type(listObj))
    listObj.append({
      "type": "insurance",
      "insurance_code": self.insurance_code,
      "insurance_name": self.insurance_name,
      "insurance_type": self.insurance_type,
      "insurance_desc": self.insurance_desc,
      "insurance_value": self.insurance_value,
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