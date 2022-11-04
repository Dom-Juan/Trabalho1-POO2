import random


class Property:
  def __init__(self,
               address: str,
               construction_date: str,
               total_area: float,
               constructed_area: float,
               num_rooms: int,
               num_bathrooms: int,
               num_spots_garage: int,
               iptu: float,
               property_worth: float,
               property_rent: float):
    self._property_code: int = random.randint(0, 9999)
    self._address: str = address
    self._total_area: float = total_area
    self._constructed_area: float = constructed_area
    self._construction_date: str = construction_date
    self._num_rooms: int = num_rooms
    self._num_bathrooms: int = num_bathrooms
    self._num_spots_garage: int = num_spots_garage
    self._iptu: float = iptu
    self._property_worth: float = property_worth
    self._property_rent: float = property_rent

  @property
  def property_code(self):
    return self._property_code

  @property_code.setter
  def property_code(self, value):
    self._property_code = value
    pass

  @property
  def address(self):
    return self._address

  @address.setter
  def address(self, value):
    self._address = value
    pass

  @property
  def total_area(self):
    return self._total_area

  @total_area.setter
  def total_area(self, value):
    self._total_area = value
    pass

  @property
  def constructed_area(self):
    return self._constructed_area

  @constructed_area.setter
  def constructed_area(self, value):
    self._constructed_area = value
    pass

  @property
  def construction_date(self):
    return self._construction_date

  @construction_date.setter
  def construction_date(self, value):
    self._construction_date = value
    pass

  @property
  def num_rooms(self):
    return self._num_rooms

  @num_rooms.setter
  def num_rooms(self, value):
    self._num_rooms = value
    pass

  @property
  def num_bathrooms(self):
    return self._num_bathrooms

  @num_bathrooms.setter
  def num_bathrooms(self, value):
    self._num_bathrooms = value
    pass

  @property
  def num_spots_garage(self):
    return self._num_spots_garage

  @num_spots_garage.setter
  def num_spots_garage(self, value):
    self._num_spots_garage = value
    pass

  @property
  def iptu(self):
    return self._iptu

  @iptu.setter
  def iptu(self, value):
    self._iptu = value
    pass

  @property
  def property_worth(self):
    return self._property_worth

  @property_worth.setter
  def property_worth(self, value):
    self._property_worth = value
    pass

  @property
  def property_rent(self):
    return self._property_rent

  @property_rent.setter
  def property_rent(self, value):
    self._property_rent = value
    pass