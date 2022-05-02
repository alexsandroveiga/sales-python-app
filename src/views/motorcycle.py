from database import motorcycleRepo
from adapters import adaptResponse, adaptInput, adaptTable

def menu ():
  print("""
  1. Adicionar uma motocicleta
  2. Remover um motocicleta
  3. Atualizar dados de uma motocicleta
  4. Exibir todas as motocicletas
  5. Exibir uma motocicleta
  6. Voltar ao menu anterior
  """)

def motorcycleView ():
  while True:
    menu()
    option = input('Escolha uma opção: ')
    if option == '1':
      motorcycle = adaptInput(['Marca', 'Modelo', 'Preço', 'Cilindrada', 'Potência Máxima'])
      motorcycleRepo.create(motorcycle)

    if option == '2':
      email = input('Digite o email: ')
      try:
        motorcycleRepo.delete(email)
        adaptResponse({ 'message': 'Cliente removido com sucesso'})
      except:
        adaptResponse({ 'message': 'Ocorreu um erro ao remover o cliente' })   

    if option == '3':
      break

    if option == '4':
      adaptTable('Motos', ['Marca', 'Modelo', 'Preço'], motorcycleRepo.find())

    if option == '5':
      email = input('Digite o email: ')
      adaptResponse(motorcycleRepo.findOne(email))

    if option == '6':
      break

