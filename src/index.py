from database import createTables
from views import customerView, motorcycleView

def mainMenu ():
  print("""
  1. Gerenciar clientes
  2. Gerenciar motocicletas
  3. Vendas de motocicletas
  4. Consultas específicas
  5. Sair
  """)

while True:
  createTables()
  mainMenu()
  option = input('Escolha uma opção: ')

  if option == '1':
    customerView()

  if option == '2':
    print('Escolheu a opção 2')
    motorcycleView()

  if option == '3':
    print('Escolheu a opção 3')
    break

  if option == '4':
    print('Escolheu a opção 4')
    break

  if option == '5':
    print('Escolheu a opção 5')
    break