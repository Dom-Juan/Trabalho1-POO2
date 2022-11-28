import json
import sys

import PySimpleGUI as sg

from os import path
from datetime import datetime
from datetime import timedelta
from classes.money.payment import Payment
from classes.property.property import Property
from classes.user.user_broker import UserBroker
from classes.user.user_client import UserClient

sys.path.append('../')
sys.path.append('../')


class RentMade:

    def __init__(self, rent_code: int, client: UserClient, broker: UserBroker, prop: Property, rent_date: datetime,
                 devolution_date: datetime, payment_date: datetime, total_rent_amount: float, payment_method: Payment,
                 insurance_hired: list, paid: bool):
        self._rent_code: int = rent_code
        self._client: UserClient = client
        self._broker: UserBroker = broker
        self._prop: Property = prop
        self._rent_date: datetime = rent_date
        self._devolution_date: datetime = devolution_date
        self._payment_date: datetime = payment_date
        self._total_rent_amount: float = total_rent_amount
        self._payment_method: Payment = payment_method
        self._insurance_hired: list = insurance_hired
        self._paid: bool = paid
        self._layout = []

    @property
    def rent_code(self):
        return self._rent_code

    @rent_code.setter
    def rent_code(self, value):
        self._rent_code = value

    @property
    def client(self):
        return self._client

    @client.setter
    def client(self, value):
        self._client = value

    @property
    def broker(self):
        return self._broker

    @broker.setter
    def broker(self, value):
        self._broker = value

    @property
    def prop(self):
        return self._prop

    @prop.setter
    def prop(self, value):
        self._prop = value

    @property
    def rent_date(self):
        return self._rent_date

    @rent_date.setter
    def rent_date(self, value):
        self._rent_date = value

    @property
    def devolution_date(self):
        return self._devolution_date

    @devolution_date.setter
    def devolution_date(self, value):
        self._devolution_date = value

    @property
    def payment_date(self):
        return self._payment_date

    @payment_date.setter
    def payment_date(self, value):
        self._payment_date = value

    @property
    def total_rent_amount(self):
        return self._total_rent_amount

    @total_rent_amount.setter
    def total_rent_amount(self, value):
        self._total_rent_amount = value

    @property
    def payment_method(self):
        return self._payment_method

    @payment_method.setter
    def payment_method(self, value):
        self._payment_method = value

    @property
    def insurance_hired(self):
        return self._insurance_hired

    @insurance_hired.setter
    def insurance_hired(self, value):
        self._insurance_hired = value

    @property
    def paid(self):
        return self._paid

    @paid.setter
    def paid(self, value):
        self._paid = value

    def calc_total_amount(self):
        contract_time: timedelta = self._devolution_date - self._rent_date
        return self._total_rent_amount * int(contract_time.days / 30)

    def has_insurance(self):
        return bool(self._insurance_hired)

    def is_late(self):
        if self._paid:
            return False
        if self._payment_date < datetime.now():
            return True
        return False

    def print_obj(self):
        self._layout = [
            [sg.Text(self.rent_code)],
            [sg.Text(self._client)],
            [sg.Text(self._broker)],
            [sg.Text(self._prop)],
            [sg.Text(self._rent_date)],
            [sg.Text(self._devolution_date)],
            [sg.Text(self._payment_date)],
            [sg.Text(self._insurance_hired)],
            [sg.Text(self._paid)],
            [sg.Button('Ok')]
        ]
        window = sg.Window("Print do Aluguel", self._layout, size=(640, 480), resizable=True, modal=True)
        while True:
            event, values = window.read()
            if event in ["Exit", sg.WIN_CLOSED, "Ok"]:
                break
        window.close()

    def save_json_file(self):
        filename = './files/rent_data.json'
        if path.isfile(filename) is False:
            raise Exception("File not found")
        with open(filename) as fp:
            listObj = json.load(fp)
        print(listObj)
        for item in listObj:
            if item['rent_code'] == self._rent_code:
                print("Aluguel já registrado")
                listObj.remove(item)
        print(type(listObj))
        listObj.append({
            "_rent_code": self._rent_code,
            "_client": self._client,
            "_broker": self._broker,
            "_prop": self._prop,
            "_rent_date": self._rent_date,
            "_devolution_date": self._devolution_date,
            "_payment_date": self._payment_date,
            "_total_rent_amount": self._total_rent_amount,
            "_payment_method": self._payment_method,
            "_insurance_hired": self._insurance_hired,
            "paid": self._paid
        })
        print(listObj)
        with open(filename, 'w', encoding='utf-8') as json_file:
            json.dump(listObj, json_file,
                      indent=4,
                      separators=(',', ': '),
                      ensure_ascii=True)
        print('> Arquivo JSON atualizado com sucesso!')
