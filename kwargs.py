# def ai(**kwargs):
#      print(kwargs)
# ai(name='Dastan',surname="Ashyralyev",age=16)

# def ai(*args,**kwargs):
#   for k in range (1,2,1):
#     print("ваше имя",kwargs["name"])
#     print("ваше  фамилие",kwargs["surname"])
#     print("ваш возрост",kwargs["age"])
#     print("ваш номер кв", args[0])
#     print("ваш город проживание", args[1])
#
# ai(46,"Бишкек",name="Arsen", surname="Kubandykov" , age=32)

# def ai(*args,**kwargs):
#   a = 0
#   while a < 1 :
#     a = a + 1
#     print("ваше имя",kwargs["name"])
#     print("ваше  фамилие",kwargs["surname"])
#     print("ваш возрост",kwargs["age"])
#     print("ваш номер кв", args[0])
#     print("ваш город проживание", args[1])
# ai(46,"Бишкек",name="Arsen", surname="Kubandykov" , age=32)

# def ai(**kwargs):
#     for a in kwargs:
#      if a == 18  :
#              print("добро пожаловать!")
#      else:
#              print("доступ завершон")
# ai(name="Arsen", surname="Kubandykov" , age=24)


# def  greet(*args,**kwargs):
#     for i in args:
#         print(f' {i} привет')
# greet("нурел","адилет","курсант")

# def оценки(*args,**kwarg):
#     for i in args:
#          print(f"средный бал:{kwarg["имя"]}:{i}")
# оценки(3,4,5,имя="курсант")

# def online_shop(*args, **kwargs):
#     for i in args:
#         print(f"Online shop:{kwargs["имя"]} купил {i}")
#     print(f"обшый сумма{kwargs["сумма"]}")
# online_shop("молоко,хлеб,яйцо",имя="нурел",город="жалал-абад",сумма="250 сом")

# def online_food_order(*args, **kwargs):
#     for i in args:
#         print(f"имя покупателя:{kwargs["имя"]};адрес покупателя:{kwargs["адрес"]};Что вы купили?{i}")
# online_food_order("пицца,суши",имя="адилет",адрес="жапа-салды 36 дом")
















































