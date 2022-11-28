import json

from os import path
from classes.money.payment import Payment


class RealStateCompany:
    def __init__(self, name: str, address: str, rentals: list, sales: list, properties: list, users: list,
                 insurances: list, config: any):
        self.__name: str = name
        self.__address: str = address
        self.__rentals: list = rentals
        self.__sales: list = sales
        self.__properties: list = properties
        self.__users: list = users
        self.__insurance: list = insurances
        self.__config: any = config

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value
        pass

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, value):
        self.__address = value
        pass

    @property
    def rentals(self):
        return self.__rentals

    @rentals.setter
    def rentals(self, value):
        self.__rentals = value
        pass

    @property
    def sales(self):
        return self.__sales

    @sales.setter
    def sales(self, value):
        self.__sales = value
        pass

    @property
    def real_state_properties(self):
        return self.__properties

    @real_state_properties.setter
    def real_state_properties(self, value):
        self.__properties = value
        pass

    @property
    def users(self):
        return self.__users

    @users.setter
    def users(self, value):
        self.__users = value
        pass

    @property
    def insurance(self):
        return self.__insurance

    @insurance.setter
    def insurance(self, value):
        self.__insurance = value
        pass

    @property
    def config(self):
        return self.__config

    @config.setter
    def config(self, value):
        self.__config = value
        pass

    def save_json_file(self) -> str:
        filename = './files/real_state_company_data.json'
        if path.isfile(filename) is False:
            return "> File not found"
            raise Exception("File not found")
        # Lendo o arquivo json
        with open(filename) as fp:
            listObj = json.load(fp)
        print(listObj)
        for item in listObj:
            if item['name'] == self.name:
                print("Imobiliária já existe!")
                listObj.remove(item)
        print(type(listObj))
        listObj.append({
            "type": "real_state_company",
            "name": self.__name,
            "address": self.__address,
            "config": self.__config,
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

    # Adicionar um novo obj a lista de obj.
    def add_rental(self, rental):
        self.__rentals.append(rental)
        pass

    def add_sales(self, sale):
        self.__sales.append(sale)
        pass

    def add_real_state_properties(self, properties):
        self.__properties.append(properties)
        pass

    def add_user(self, user):
        self.__users.append(user)
        pass

    def add_insurance(self, insurance):
        self.__insurance.append(insurance)
        pass
    # Fim da classe.
