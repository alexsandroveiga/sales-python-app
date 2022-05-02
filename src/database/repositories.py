from .entities import Customer, Motorcycle

class Repository:
  def __init__(self, model):
    self.model = model

  def findAll(self):
    return list(self.model.select().dicts())

  def findById(self, id):
    return self.model.get_or_none(id=id)

  def create(self, data):
    return self.model.create(**data)

  def update(self, id, data):
    return self.model.update(**data).where(self.model.id == id).execute()

  def delete(self, id):
    return self.model.delete().where(self.model.id == id).execute()

class CustomerRepository:
  def find(self):
    customers = list(Customer.select(*[Customer.id, Customer.name, Customer.email, Customer.phone]).dicts())
    return customers

  def create(self, input):
    customer = Customer.create(**input).__data__
    return customer

  def findOne(self, email):
    customer = Customer.get(Customer.email == email).__data__
    return customer

  def delete(self, email):
    customer = Customer.get(Customer.email == email)
    customer.delete_instance()

customerRepo = CustomerRepository()

class MotorcycleRepository(Repository):
  def __init__(self):
    super().__init__(Motorcycle)

  def find(self):
    motorcycles = list(Motorcycle.select(*[Motorcycle.brand, Motorcycle.model, Motorcycle.price]).dicts())
    return motorcycles

motorcycleRepo = MotorcycleRepository()