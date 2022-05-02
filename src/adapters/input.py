def adaptInput (fields):
  object = {}
  for field in fields:
    if (field == 'Nome'): object['name'] = input(field + ': ')
    if (field == 'Email'): object['email'] = input(field + ': ')
    if (field == 'Sexo'): object['gender'] = input(field + ': ')
    if (field == 'CPF'): object['identifier'] = input(field + ': ')
    if (field == 'Endereço'): object['address'] = input(field + ': ')
    if (field == 'Telefone'): object['phone'] = input(field + ': ')
    if (field == 'Estado'): object['state'] = input(field + ': ')
    if (field == 'Cidade'): object['city'] = input(field + ': ')
    if (field == 'CEP'): object['zip_code'] = input(field + ': ')
    if (field == 'Marca'): object['brand'] = input(field + ': ')
    if (field == 'Modelo'): object['model'] = input(field + ': ')
    if (field == 'Preço'): object['price'] = input(field + ': ')
    if (field == 'Cilindrada'): object['engine_capacity'] = input(field + ': ')
    if (field == 'Potência Máxima'): object['maximum_power'] = input(field + ': ')
  return object