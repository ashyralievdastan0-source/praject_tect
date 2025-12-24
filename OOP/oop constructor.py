# class Car:
#     # поля
#     model = "Ford"
#     color = "Black"
#     age = 2023
#     country = "USA"
#     #метод кыймыл аракет
#     def start(self):
#         return ("стартуй заводи матор")
#     def move(self):
#         return ("начат движение")
#     def stop(self):
#         return ("стоп на месте и выключи двигатель")
#     #
# car = Car()
# print(car.start())
#
# class User:
#     def __init__(self,name,age,email):
#         self.name=name
#         self.age=age
#         self.email=email
#     def info(self):
#         return  f"Твое имя:{self.name}\nТвой возраст:{self.age}\nТвой емаил:{self.email}"
#     def is_adult(self):
#         if self.age<18:
#             return "Вы несовершеннолетний"
#         else:
#             return f" Вам {self.age} лет"
#     def change_email(self,new_email):
#         if self.email != new_email:
#             self.email = new_email
#             return f"Email изменен на {new_email}"
# user = User( "dastan",16,"ashyralyev")
# print(user.info())
# print(user.is_adult())
# print(user.change_email ("ashyraluev"))

# class Car:
#     def __init__(self, brand, model, year,color):
#         self.brand = brand
#         self.model = model
#         self.year = year
#         self.color = color
#     def describe(self):
#         return f'марка машина{self.brand}\n модел машина {self.model} \n год машина{self.year}\n цвет машина {self.color}'
#     def repaint(self,new_color):
#         if self.color != new_color:
#           self.color = new_color
#           return f"цвет изменен на {new_color}"
#     def year(self):
#         car_year = self.year - self.year
#         return f"автомобил {car_year} лет"
# car = Car("BMW", "bmw", 2023, "blue")
# print(car.describe())
# print(car.year())
# print(car.repaint("black"))


#   ИНПАКСУЛЯЦИЯ  ООП
# class Car:
#     def __init__(self, model , year, color):
#         self.__model = model
#         self.__year = year
#         self.__color = color
#
#
#     def get(self):
#         return f"маалымат алынды  {self.__model}"
#     def get1(self):
#         return f"2 маалымат алынды  {self.__color}"
#
#
#     def set(self, new_model):
#         self.__model = new_model
#         return f"новая модель обнавлен  {self.__model}"
#
#
# car = Car("BMW",2020,"black")
# print(car.get())
# print(car.get1())
# print(car.set("Mers"))

# class User:
#     def __init__(self,age):
#         self.age = age
#     def age (self):
#         return self.age
#     def age(self,value):
#         if 0 <= value <= 120:
#             return f"некорректный возраст"
# user = User(20)
# user.age(20)
# print(user.age(20))
# print(user.age(20))

# class Laptop(object):
#     def __init__(self, brent,model,ram,storage):
#         self.brent=brent
#         self.model=model
#         self.ram=ram
#         self.storage=storage
#     def show(self):
#         print("BRENT:",self.brent)
#         print("MODEL:",self.model)
#         print("RAM:",self.ram)
#         print("STORAGE:",self.storage)
#     def hide(self):
#         if


# class Laptop:
#     def __init__(self, brand, model, ram, storage):
#         self.__brand = brand
#         self.__model = model
#         self.ram = ram
#         self.storage = storage
#
#     @property
#     def ram(self):
#         return self.__ram
#
#     @ram.setter
#     def ram(self, value):
#         allowed_ram = {4, 8, 16, 32}
#         if value in allowed_ram:
#             self.__ram = value
#         else:
#             raise ValueError(f"Недопустимое значение RAM: {value}. Разрешено: {allowed_ram}")
#
#     @property
#     def storage(self):
#         return self.__storage
#
#     @storage.setter
#     def storage(self, value):
#         allowed_storage = {128, 256, 512, 1024}
#         if value in allowed_storage:
#             self.__storage = value
#         else:
#             raise ValueError(f"Недопустимое значение хранилища: {value}. Разрешено: {allowed_storage}")
#
#     def info(self):
#         return (f"Ноутбук: {self.__brand} {self.__model} | "
#                 f"RAM: {self.__ram} ГБ | Хранилище: {self.__storage} ГБ")
#
#     def upgrade_ram(self, new_ram):
#         try:
#             temp_ram = new_ram
#         except ValueError as e:
#             print(f"Ошибка обновления RAM: {e}")
#             return
#
#         if new_ram > self.__ram:
#             self.ram = new_ram
#             print(f"RAM успешно обновлена до {new_ram} ГБ.")
#         else:
#             print(f"Обновление не требуется: {new_ram} ГБ не больше текущих {self.__ram} ГБ.")
# try:
#     my_laptop = Laptop("Dell", "XPS 13", 8, 512)
#     print(my_laptop.info())
# except ValueError as e:
#     print(f"Ошибка при создании объекта: {e}")
#
# print("-" * 20)
# my_laptop.upgrade_ram(16)
# print(my_laptop.info())
#
# print("-" * 20)
# my_laptop.upgrade_ram(8)
# print(my_laptop.info())
#
# print("-" * 20)
#
# my_laptop.upgrade_ram(12)
# print(my_laptop.info())
#
# print("-" * 20)
#
# try:
#     another_laptop = Laptop("HP", "Spectre", 16, 1000)
#     print(another_laptop.info())
# except ValueError as e:
#     print(f"Ошибка при создании объекта: {e}")

# class User:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def __name__(self):
#         return self.name
#     def age(self):
#             return f"некорректный возраст{if age > 18}"
# n=User( 100)
# print(n.__name__)













































































































        




