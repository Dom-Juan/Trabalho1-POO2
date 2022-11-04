def check_if_all_none(list_of_elem):
  """ Verifica se algum elemento da lista é None """
  result = True
  for elem in list_of_elem:
    if elem is not None:
      return False
  return result

def check_if_all_empty(list_of_elem):
  """ Verifica se algum elemento da lista é None """
  result = True
  for elem in list_of_elem:
    if elem is not '':
      return False
  return result