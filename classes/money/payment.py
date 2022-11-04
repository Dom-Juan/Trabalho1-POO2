import uuid


class Payment:
  def __init__(self, payment_type: str):
    self.__insurance_code: int = uuid.uuid1().int
    self._payment_type: str = payment_type
    pass

  @property
  def payment_type(self):
    return self._payment_type

  @payment_type.setter
  def payment_type(self, value):
    self._payment_type = value
    pass

  @property
  def payment_code(self):
    return self._payment_code

  @payment_code.setter
  def payment_code(self, value):
    self._payment_code = value
    pass