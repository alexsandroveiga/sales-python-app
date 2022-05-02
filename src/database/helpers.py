from . import Customer, Motorcycle, database

def createTables():
  with database:
    database.create_tables([Customer, Motorcycle])