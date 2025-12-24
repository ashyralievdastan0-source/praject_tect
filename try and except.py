# try:
#     a = int(input("Enter a number: "))
#     print(4/a)
# except:
#         print("не правилна")

# try:
#     a = int(input('Enter a number: '))
#     if 8 / a :
#         print('Yes')
#     else:
#         print('No')
# except:
#     print('Something went wrong')

# try:
#     n = int(input('Enter a number: '))
#     a = input("Enter a opereshen: ")
#     b = int(input("Enter another number: "))
#     if a == "+":
#         print(n + b)
#     elif a == "-":
#         print(n - b)
#     elif a == "*":
#         print(n * b)
#     elif a == "/":
#             print(n / b)
#     else:
#         print("Invalid input")
# except ZeroDivisionError:
#     print("нелзя исползиват 0")


# for i in range(11):
#     print(i)
# a = 1
# while a <=10:
#     print(a)
#     a += 1
#
# a = [1, 2, 3]
#
# b = {1,2,3}
#
# c = (1,2,3)
#
# k = dict(a=1,b=2,c=3)





















# a = []
# b = []
# try:
#     a.append(1)
#     b.append(2)
#     print(a)
#     print(b)
#     c = int(input("Enter a number: "))
#     for i in range(1,10):
#          a.append(i)
#
#          if i % 2 == 0:
#           b.append(i)
#          elif i % 2 != 0:
#            b.append(i)
#          else:
#             print("dgfhd")
# except:
#     print("dgfhd")

# try:
#     a = []
#     b = []
#     for x in range(1,10):
#         c = (input("Enter a number: "))
#         if x % 2 == 0:
#             a.append(c)
#         b.append(c)
#     print(a,b)
# except:
#     print("Invalid input")

# try:
#   b = []
#   print("1 довабит элемент в списокy")
#   print("2 удалит элемент")
#   print("3 показат список")
#   print("4 выход")
#   while True:
#     a = int(input("введите цифра"))
#     if a == 1:
#         c = input("введите элемент")
#         b.append(c)
#         print("элемент даваблен")
#     elif a == 2:
#         d = input("введите элемент")
#         b.pop(b.index(d))
#         print("элемен удален")
#     elif a == 3:
#         print(b)
#     elif a == 4:
#         print("выход")
#         break
# except:
#     print("cfdrtd")


# def validate_email(email):
#  try:
#     a = input("Введите действительный адрес электронной почты")
#     if len(email) < 5:
#         print("Извините, ваш адрес электронной почты слишком короткий.")
#     elif len(email) > 6:
#         print("email норм")
#     else:
#         print("Извините, ваш адрес электронной почты действителен.")
#  except:
#      print("Извините, ваш адрес электронной почты недействителен")
# validate_email(''

# n = 0
# b = int(input("введите число"))
# b = b*b
# print(b)
# while n != b:
#     print(i)
#     if(i == b):
#         print(i)
#         continue
#     else:
#         print(i)
#         continue

# # n = 0
# # while True:
# #   a = (input("Enter a number: "))
# #   if a == "exit":
# #      print(f"обшый сумма {total}")
# #      break
# #   try:
# #         total = int(a)+n
# #         n = total
# #
# #   except :
# #      print("Something went wrong")
# l = []
# while True:
#     try:
#      a = (input("Enter a number: "))
#      if a == "exit":
#          print(sorted(l))
#          break
#      l.append(int(a))
#      sorted(l)
#     except:
#         print("Enter a number")
#
# try:
#     dict={"dastan":16,"eldoc":15}
#     a = (input("enter number"))
#     print(dict[a])
# except KeyError:
#     print("ошибка имя")
#
#





























