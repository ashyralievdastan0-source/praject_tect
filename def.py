"""
def это функция в пайтоне
имеет в себе очень важную роль
функции пишется для  того чтобы занимимать мало место в коде
и определенную логику проекта
одну функцию мы можем использовать не сколько раз
в разных местах проекта
"""
# from itertools import count

# def plus(a,b):
#     print("result",a,"+",b,"=",a+b)
# plus(6,3)

# def plus(adilet,elaman):
#     print("эламан мн адилеттин алмалары кошулса  ",adilet+elaman)
# plus(4,8)

# def mines(a ,b):
#     if a == b:
#         print("yes")
#     else:
#         print("no")
# mines(1,2)

# def grade(score):
#     if score >= 90 and  score <= 100:
#         print("отлично")
#     elif score >= 70 and score <= 89:
#         print("хорошо")
#     elif score>= 50 and score <= 69:
#         print("Удовлетворительно")
#     elif score < 50:
#         print("плохо")
#     else:
#         print("такого число нет")
# grade(-90)

"""
используйте функцию 
температура воды
если меньше 0 минус вывод холодный
если больше 100 гр кипящий 
else пар 
использовать инт(инпут для ввода температуры напишите введите градус)
"""

# def temperatura():
#     a = int(input("введите градус"))
#     if a <= 0 :
#         print("холодный")
#     elif a <= 50 and a > 0 :
#         print("теплая")
#     else:
#         print("пар")
# temperatura()

"""
задание 3
программа для подсчета положительных чисел
создайте функцию count_positive 
которая спрашивает у пользователя 5 чисел и считает
сколько из них положительные число и их количество

"""


# def count_positive(b,c):
#     for d in range(5):
#       a = int(input("введите число"))
#       if a > 0:
#           print()
#           b = b + 1
#       else:
#           print()
#           c = c + 1
#     print("число отрицателный",c)
#     print("число положительный",b)
# count_positive(0,0)

# def count_negative():
#     a = int(input("введите число"))
#     for d in range(1,11):
#         print(a,"*",d,"=",a*d)
# count_negative()

# def parol():
#     a = 20090223
#     for i in range(3):
#      d = int(input("введите пароль"))
#      if d == a:
#          print("правильна")
#          break
#      else:
#          print("не правильна")
# print("у тебя больше нет попытка")
# parol()

# def product():
#     print("1 добавит покупку")
#     print("2 показат список ")
#     print("3 удалит покупку")
#     print("4 посчитать обшую сумму")
#     print("5 выйти")
# def count():
#     d = {"яблоко":"125","молоко":"40","яйцо":"15"}
#     while True:
#          a = input("что вам нужна")
#          if a == "1":
#              b = input("введите продукты ")
#              c = input("введите цена")
#              d[b] = c
#              print("продукта добовлен")
#              def das():
#               if d == "2":
#                 print("список",d)
#
#               # def main():
#               #       if a == 3:
#               #           e = input("удалит продукта")
#               #           d[e]= "0"
#               #           main(
#              das()
# count()
# product()

#
# s = {}
# def will_add_a_product():
#     b = input("введите продукта")
#     c = int(input("введите цена"))
#     s[b]=c
#     print("продукта добовлен")
# def show_():
#         print(s)
# def remove_product():
#     if  s:
#         d = input("имя продук")
#         del s[d]
#         print("продукта удалено")
#     else:
#         print("Такого продукта нет.")
# def pilus():
#     n = sum(s.values())
#     print("обшая сумма продукта",n)
# def show_total():
#         print("выхот")
# def everything():
#     while True:
#         print("1 добавит покупку")
#         print("2 показат список ")
#         print("3 удалит покупку")
#         print("4 посчитать обшую сумму")
#         print("5 выйти")
#         a = int(input("введите "))
#         if a == 1:
#             will_add_a_product()
#         elif a == 2:
#             show_()
#         elif a == 3:
#             remove_product()
#         elif a == 4:
#             pilus()
#         elif a == 5:
#             show_total()
#             break
#
# everything()




# def chacking_password():
#     password = input("введите пароль!")
#     number = False
#     char = False
#     for chars in password:
#         if chars.isdigit():
#             number = True
#
#         if chars.isalpha():
#             char = True
#     if len(password) >= 6 and number and char:
#         print("надежный пароль успешно")
#     elif number == False:
#         print("нет чисел добавьте числа")
#     elif char == False:
#         print("нет символов добавьте символы")
#     else:
#         print("пароль слабый :  чтобы был надежный пароль должно быть больще 6 символов")
# chacking_password()


# password = input("введите пароль!")
# number = False
# char = False
# for chars in password:
#     if chars.isdigit():
#         number = True
#
#     if chars.isalpha():
#         char = True
# if len(password) >= 6 and number and char:
#         print("надежный пароль успешно")
# elif number == False:
#         print("нет чисел добавьте числа")
# elif char == False:
#         print("нет символов добавьте символы")
# else:
#         print("пароль слабый :  чтобы был надежный пароль должно быть больще 6 символов")


# def calculate(*args):
#     total = 0
#     if total :
#         print(f"totalPrice{total}")
#     for i in args:
#             total += i
# calculate(65,654)

# def add_purchase(purchase_list):
#     item = input("Enter item name: ")
#     price = int(input("Enter price: "))
#     purchase = {"item": item, "price": price}
#     purchase_list.append(purchase)
#     print("Purchase added!")
# def show_list(purchase_list):
#     if not purchase_list:
#         print("The shopping list is empty.")
#     else:
#         i = 0
#         while i < (purchase_list):
#             purchase = purchase_list[i]
#             print((i + 1) + "." + purchase["item"] + "-" + (purchase["price"]) + "som")
#             i += 1
# def remove_purchase(purchase_list):
#     show_list(purchase_list)
#     if purchase_list:
#         number = int(input("Enter the number of the purchase to remove: "))
#         if 1 <= number <=(purchase_list):
#             removed = purchase_list.pop(number - 1)
#             print("Removed: " + removed["item"])
#         else:
#             print("Invalid number!")
# def total_sum(purchase_list):
#     total = 0
#     i = 0
#     while i < (purchase_list):
#         total += purchase_list["price"]
#         i += 1
#     print("Total sum: " +  + "som")
# def main_menu():
#     shopping_list = []
#     while True:
#         print("--- Choose an action ---")
#         print("1 - Add a purchase")
#         print("2 - Show shopping list")
#         print("3 - Remove a purchase")
#         print("4 - Calculate total sum")
#         print("5 - Exit")
#         choice = input("Your choice: ")
#         if choice == "1":
#             add_purchase(shopping_list)
#         elif choice == "2":
#             show_list(shopping_list)
#         elif choice == "3":
#             remove_purchase(shopping_list)
#         elif choice == "4":
#             total_sum(shopping_list)
#         elif choice == "5":
#             print("Exiting program. Goodbye!")
#             break
#         else:
#             print("Invalid input. Please choose from 1 to 5.")

# main_menu()
#
#
# def calculate(*args):
#     string = ""
#
#     for i in args:
#         far = len(i)
#
#     print("самая длинная", i)
#
#
# calculate("apple", "orange", "banana", "chair", )

# def сумма_чисел(*args):
#     total = 0
#     for arg in args:
#         if arg > 0:
#             print(arg)
#             total += arg
# сумма_чисел(1,2,5,4,7,6,8,7,)

# def слова(*args):
#     a = len(args)
#     for args in args:
#            print(a)
# слова(len,"молоко","хлеб","число")

# def min_max(*args):
#     a = min(args)
#     b = max(args)
#     for arg in a:
#         print(a,b)
# min_max(23,12,32,21,54,45)
#
# def  analysis(*args):
#     a = max(args)
#     for i in args:
#           print(a)
# analysis("milk","cat","whele")

# def culculate(*args):
#     total = 0
#     for g in args:
#         if g % 2 == 0:
#             total += 1
#     print(f"количество четных - {total}")
# culculate(3,6,5,2,8)

# def min_max(*args):
#     for a in args:
#         if  a == max(args) or a == min(args):
#           print(a)
# min_max(23,12,32,21,54,45)

# def  analysis(*args):
#     for i in args:
#         if i > min(args) and i < max(args):
#           print(i)
# analysis("milk","cat","whele")


# def  analysis(*args):
#     return "".join(args)
# a  = analysis("молоко","яблоко","мука")
# print(a)























