# def bsort(a):
#     length = len(a)
#     for i in range(length):
#         for j in range(0, length-i-1):
#             if  a[j] > a[j+1]:
#                 temp = a[j]
#                 a[j] = a[j + 1]
#                 a[j + 1] = temp
#     print(a)
# #    1 2 3 4 5 6 7 8 9
# #    1 3 2 5 4 7 6 8 9
# a = [3,1,5,2,7,4,6,9,8]
# bsor(a)

# def bsort(a):
#     n = len(a)
#     for i in range(n):
#         for j in range(0, n-i-1):
#             if a[j] > a[j+1]:
#                 a[j], a[j+1] = a[j+1], a[j]
#     print(a)
# a = [7,4,3,9,8,6,5,4,3,22,]
# bsort(a)

# def insertion_sorted(arr):
#     for i in range(len(arr)):
#         key = arr[i]
#         j = i
#         while j > 0 and key < arr[j-1]:
#             arr[j] = arr[j-1]
#             j -= 1
#             arr[j] = key
#     print(arr)
# arr = [5,7,2,4,9,1,3,8,6]
# insertion_sorted(arr)
#
# def  sorted_in(n):
#      return sorted([n[i]
#      for i in range(1,len(n),2)])
# print(sorted_in([1,2,3,4,5,6,7,8,9]))

# def even_odd(n):
#     for i in range(0,n,2):
#         if i%2==0 and i%2==0:
#                 print(i,end=" ")
#         else:
#                 print(i,end=" ")
#     print(n)
# n = 12,31,42,35,65
# print(even_odd(n))

# def even_odd(n):
#     even = []
#     odd = []
#     for i in range(n):
#         if i % 2 == 0:
#             even.append(i)
#         else:
#             odd.append(i)
#     print("even",even)
#     print("odd",odd)
# print(even_odd(67))

# def find_number(lst):
#     a = int(input("введите число"))
#     nums = [10,5,20,3,7]
#     for num in nums:
#         if num in lst:
#             print("yes ")
#         else:
#             print("no")
# print(find_number([10,5,20,3,7]))

# def find_number(lst):
#     a = int(input("введите число"))
#     nums = [10,5,20,3,7]
#     for num in nums:
#         if a in lst:
#             print("число найдена")
#         else:
#             print("нет в списке ")
# print(find_number([10,5,20,3,7]))

# def find_number(lst):
#     a = int(input("введите число"))
#     for num in nums:
#         if a in lst:
#             print("число найдена")
#         else:
#             print("нет в списке ")
# nums = [10,5,20,3,7]
# print(find_number(nums))

# def find_number(lst):
#     a = int(input("Enter a number: "))
#     for num in lst:
#         if num == a:
#             return num
#         else:
#             continue
# num = [10,5,29,3,7,4]
# print(find_number(num))



















