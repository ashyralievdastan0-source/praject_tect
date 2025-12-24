# class Animal:
#     def __init__(self,voice,organs,colors,ves):
#         self.voice = voice
#         self.organs = organs
#         self.colors = colors
#         self.ves = ves
#     def Animal_voice(self):
#         return "голос"
#     def move(self):
#         return "старт движение"
#     def slip(self):
#         return "спать"
# class Dog(Animal):
#     def __init__(self,voice,organs,colors,ves,name,):

# class Animal:
#     def __init__(self, voice, organs, colors, ves,):
#         self.voice = voice
#         self.organs = organs
#         self.colors = colors
#         self.ves = ves
#     def Animal_voice(self):
#         return "голос"
#     def move(self):
#         return "начать движение"
#     def slip(self):
#         return "спать"
#
# class Dog(Animal):
#     def __init__(self ,voice, organs, colors, ves, name_dog,poroda, gender):
#         self.voice = voice
#         self.organs = organs
#         self.colors = colors
#         self.ves = ves
#         self.name_dog = name_dog
#         self.poroda = poroda
#         self.gender = gender
#
#     def dog_voice(self):
#         return f"{self.voice}"
#     def move_dog(self):
#         return f"start moveing{self.name_dog}"
#     def slip_dog(self):
#         return "спать"
#
#
# dog = Dog("gaf - gaf", "brain", "black",
#           "8кг",
#           " Rex",
#           "Avcharka",
#           "man")
# print(dog.dog_voice())
# print(dog.move_dog())

# class User:
#     def __init__(self, name, surname, age,height):
#         self.name = name
#         self.surname = surname
#         self.age = age
#         self.height = height
#     def user_first_name(self):
#         return self.name
#     def user_last_name(self):
#         return self.surname
#     def user_age(self):
#         return self.age
#     def user_height(self):
#         return self.height
# user=User("dastan","ashyralyev",16,170)
# print(user.user_first_name())
# print(user.user_last_name())
# print(user.user_age())
# print(user.user_height())

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def age(self,value):
#         if 6 < value<120:
#             age = value
# class Student(Person):
#     def __init__(self, name, age, grade):
#         super().__init__(name, age)
#         self.grade = grade
#     def grade(self,value):
#         if 1 < value < 5:
#             grade = value
#     def info(self):
#         return f'Студент\nимя:{self.name}\nвозраст:{self.age}\nоценки:{self.grade}\n'
# class Teacher(Person):
#     def __init__(self, name, age, subject):
#         super().__init__(name, age)
#         self.subject = subject
#     def info(self):
#         return f"Учитель\nимя:{self.name}\nвозраст:{self.age}\nпубл:{self.subject}\n"
# student = Student("dastan","16","5")
# teacher = Teacher("Айжамал","34","Математика")
# print(student.info())
# print(teacher.info())

# class Animal:
#     def __init__(self, name, age):
#         self.name = name
#         self.__age = age
#         self.set_age = age
#     def set_age(self,value):
#         if 0 <= value <= 50:
#             self.__age = value
#     def get_age(self):
#         return self.__age
#     def info(self):
#         return f"имя:{self.name},age:{self.__age}"
# class Dog(Animal):
#     def __init__(self, name, age, breed):
#         super().__init__(name, age)
#         self.breed = breed
#     def set_breed(self):
#         return f"порода собака:{self.breed}"
#     def nfo(self):
#         return f"\nимя:{self.name}\nвозраст:{self.__age}\nпорода:{self.breed}\n"
# class Tiger(Animal):
#     def __init__(self, name, age, origin):
#         super().__init__(name, age)
#         self.origin = origin
#     def set_origin(self):
#          return self.origin
#     def fo(self):
#         return f"имя:{self.name}\nвозраст:{self.__age}\nместаположения:{self.origin}"
# animal=Animal("неизвестное животное",2)
# dog = Dog("Рекс","12","алабай")
# tiger= Tiger("тигр","17","Бразилия")
# print(animal.info())
# print(dog.info())
# print(tiger.info())

###    Объектно-ориентированное программирование (ООП)###
###   ООП принсип:
# 1 инкапцулятция,
# 2 наследования,
# 3 полиморфизмб
# 4 абстрация

# class User():
#     def __init__(self,name, surname, age):
#         self.name = name
#         self.surname = surname
#         self.age = age





# class Pets:
#     def start(self):
#         return "Dog voice"
#
# class Animal:
#     def start(self):
#         return "Cat voice"
#
#
#
# main1 = Pets()
# main2 = Animal()
# print(main1.start())
# print(main2.start())


# class Cat:
#     def Main(self ):
#         return "кот-->мяу"
# class Dog:
#     def Main(self ):
#         return "собака-->гав!"
# class Cow:
#     def Main(self ):
#         return "Cow--> мууу"
# dog = Dog()
# cat = Cat()
# cow = Cow()
# print(dog.Main())
# print(cat.Main())
# print(cow.Main())

"""адание
1) Создать базовый класс Animal

Внутри:

приватные поля: __name, __age

конструктор

геттеры / сеттеры

метод make_sound() — пустой или с обычным текстом

метод info() — выводит имя и возраст"""

# class Animal:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#     def set_name(self,value):
#         self.__name = value
#     def get_name(self):
#         return self.__name
#     def set_age(self,value):
#         self.__age = value
#     def get_age(self):
#         return self.__age
#     def make_sound(self):
#         return
# #     def info(self):
#         return f"имя:{self.__name}\nвозраст{self.__age}"
# start=Animal("tigr", 9)
# print(start.get_name())
# print(start.get_age())

"""Ученики должны:

создать 2 животных (Dog, Cat, Bird)

поменять возраст у одного (через сеттер!)

добавить их в зоопарк

вызвать метод start_show(), который выведет звуки всех животных."""

# class Animal:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def set_name(self):
#         return self.name
#     def set_age(self):
#         return self.age
# class Dog:
#     def star_show(self):
#         return "собака:гав-гаф"
# class Cat:
#     def star_show(self):
#         return "мяу-мяу"
# class Bird:
#     def star_show(self):
#         return "кар-кар"
# dog = Dog()
# cat = Cat()
# bird = Bird()
# print(dog.star_show())
# print(cat.star_show())
# print(bird.star_show())

# class Payment:
#     def __init__(self,owner,balance):
#         self.owner = owner
#         self.balance = balance
#     def set(self):
#         self.balance -= self.balance
#         return self.balance
#     def deposit(self,amount):
#         self.balance += amount
#         return self.balance
#     def pey(self,amount):
#         self.balance += amount
#         return self.balance
#     def info(self):
#         return f"{self.owner}{self.balance}"
# class Cart(Payment):
#     def pey(self,amount):
#         self.balance += amount
#         return self.balance
#     def Commission(self):
#         if self.balance - 2% self.owner.balance:
#             self.balance -= 2% self.owner.balance
    























































