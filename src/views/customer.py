from database import customerRepo
from adapters import adaptResponse, adaptInput, adaptTable

def menu ():
  print("""
  1. Adicionar um cliente
  2. Remover um cliente
  3. Atualizar dados de um cliente
  4. Exibir todos os clientes
  5. Exibir um cliente
  6. Voltar ao menu anterior
  """)

def customerView ():
  while True:
    menu()
    option = input('Escolha uma opção: ')
    if option == '1':
      customer = adaptInput(['Nome', 'Email', 'Sexo', 'CPF', 'Endereço', 'Telefone', 'Estado', 'Cidade', 'CEP'])
      customerRepo.create(customer)

    if option == '2':
      email = input('Digite o email: ')
      try:
        customerRepo.delete(email)
        adaptResponse({ 'message': 'Cliente removido com sucesso'})
      except:
        adaptResponse({ 'message': 'Ocorreu um erro ao remover o cliente' })   

    if option == '3':
      break

    if option == '4':
      adaptTable('Usuários', ['ID', 'Nome', 'Email', 'Telefone'], customerRepo.find())

    if option == '5':
      email = input('Digite o email: ')
      adaptResponse(customerRepo.findOne(email))

    if option == '6':
      break

