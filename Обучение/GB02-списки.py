# email = 'welkom@mail.ru'
# index = email.find('@')
# print(email[:index])
#
#
#
#
# name = "ПетрОв МакСим Иванович"
# print(name.lower())
# print(name.upper())
# print(name.capitalize())
# print(name.title())
# print(len(name))
# print(name.count('в'))
# print(name.split())
# # name.ljust()
# # name.rjust()
#
#
# name = "ivan"
# age = 30
# money = "200.2"
#
# print('Hello', name, 'to you', age, 'years', 'you have', money)
#
# # result = 'Hello {} to you {} years you have {}'.format(name, age, money)
# result = f'Hello {name} to you {age} years you have {money}'
# print(result)


# name = 'Sergey'
# humans = ['ivan', 'Alex', 'Olga', name]
# print(humans[::-1])


#                 Методы                         #
##################################################

# # humans.append(10)
# # humans.insert(1,200)
# humans.remove('ivan')
# print(humans.index(name))
# cut = humans.pop(0)
# print(cut)
# print(humans)
#
#
# print('Olga' in humans) # Есть или нет данное значение
#
#
# x = [1,2,3, ['sfsd','sdfsdf']]
# print(x[-1][0])
# print(x[1:])
#
#
#
# cortage = (1,2,3,4,5,6)
# cortage_list = list(cortage)
# print(cortage_list)
#
#
#
# humans = ['ivan', 'Alex', 'Olga']
#
# # x = 0
# # while x < len(humans):
# #     print(humans[x])
# #     x = x + 1
#
#
# for name in humans:
#     print(name)



# humans = {'name': 'ivan', 'age': '30', 'money': '200'}
# humans['data'] = [1,2,3,4]
# print(humans['name'])
# print(humans)
#
# print(humans.get('name'))
#
# print(humans.popitem()) #удалит последние значение и вернет кортежем
#
#
# for key in humans.keys():
#     print(key)
#
# for value in humans.values():
#     print(value )
#
# for key,value in humans.items():
#     print(key,value)
#
#
# #                 Множества                      #
# ##################################################
#
#
# my_set = {1,1,2,3,44,44,6}
# print(my_set) #выводим уникальные значения
#
#
# my_set_2 = (1,1,2,3,44,44,6)
# print(my_set_2)
# print(set(my_set_2))


# a = {1,2,3}
# b = {3,4,5}
# print(a | b) #соединение
# print(a == b) #сравнение
# print(a & b) #пересечение
# print(a - b) #разница
# print(a ^ b) #вывод все кроме пересечения



############################################################
#
#
#                      Задачи                             #



# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.


# vegs = ["банан", "яблоко", "киви", "арбуз", "egwegwegwefwefwefwef"]
#
# nums = [14, 34,32, 1,65, 10]
#
# print(max(vegs))
# print(max(vegs,key = len))

#моя версия
#

# num = 1
#
# for veg in vegs:
#     print(num, '{:>30}'.format(veg))
#     num = num + 1


# a = [10, 20, 30, 40]
# for i in enumerate(a):
#     print(i)


#без key = len будет переводить в ASCII
#
# rigth_offset = len(max(vegs, key = len ))
#
# print(rigth_offset)
#
# for index, item in enumerate(vegs, start = 1):
#     print('{}. {}'.format(index, item.rjust(rigth_offset)))


#
#
# # Задача-2:
# # Даны два произвольные списка.
# # Удалите из первого списка элементы, присутствующие во втором списке.
#

#не то
# a = {1,2,3}
# b = {3,4,5}
# print(a - b)

#
# list_a = [1,2,3,4,5,6,7]
# list_b = [3,4,5,6,7,8]
#
# # for a in list_a:
# #     print(a)
# #     list_a.remove(a)
#
# for b in list_b:
#     while b in list_a:
#         list_a.remove(b)
#
# print(list_a)


# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.
#
# new_list = []
# lists = [1,2,3,4,5,6,7,8,9]
# for list in lists:
#     if list % 2 == False:
#         list = list / 4
#         #print(list)
#     else:
#         list = list * 2
#         #print(list)
#
#     new_list.append(list)
#
# print(new_list)

#---------------------------------------------------------------

#NORMAL
# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь


# res = []
# lists = [2, -5, 8, 9, -25, 25, 4]
# for list in lists:
#     if list >= 0: #отсеяли минус
#         root = list ** 0.5
#
#         if root == int(root): #если целое
#             res.append(root)
#
# print(res)


# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)

#Решение - создать два словаря/кортежа с каждым месяцем и числом. Сплитим дату по точке и проверям число из словаря



# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random


import random
# start = -100
# stop = 100
# step = 1

# listmy = []
# i=0
# while i < 15:
#     list = random.randrange(start, stop, step)
#     listmy.append(list)
#     i = i + 1
#
# print(listmy)


# 2ой вариант

# listmy = []
# i=0
# for i in range(15):
#     list = random.randrange(start, stop, step)
#     listmy.append(list)
#

# print(listmy)



# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут:
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений: т.е. встречаются по одному разу
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]


# #a
# lst = [1, 2, 4, 5, 6, 2, 5, 2]
# print(list(set(lst))) #[1, 2, 4, 5, 6])
#
# #b
# lst2 = []
# for i in lst:
#     #print(lst.count(i)) #посчитали сколь встречается каждый элемент
#     if lst.count(i) == 1:
#         lst2.append(i)
#
# print(lst2)




