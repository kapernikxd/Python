# Ctrl + /


a = 100
b = 2
# print (a % b) остаток от деления
# print (a // b) целочисленное деление


a = 10
b = 'Text'
c = True # False
people = [10, 50, 'a']
people.append(100)
print(type(people)) #<class 'list'>
print(people)


cor = (10, 50, 'a')
print(type(cor)) #<class 'tuple'> кортеж


human = {'ivan' : 30, 'age' : 30, 'data': c}
print(type(human)) #<class 'dict'>
print(human)
print(human['ivan'])



# name = input('Ваше имя: ')
# print('Привет ', name)
#
# age = input('Ваш возраст: ')
# print('Ваш возраст ', age)



price = 100
#money = int(input('Денег в кармане: '))


# if money >= price:
#     print('Мы можем это купить')
# elif price - money <=5:
#     col = price - money
#     print('Завтра занесу', col,'рубль')
# else:
#     print('Не хватает что-то')


# name = input('Имя: ')
# surname = input('Фамилия: ')
# if name and surname:
#     print('Вы ввели и имя и фамилию')

# number = int(input('Введите число от 1 до 5: '))
#
# while number <1 or number > 5:
#     print('Неправильно, повтори')
#     number = int(input('Введите число от 1 до 5: '))
#
#
# x = 0
# while x <= 10:
#     x += 1  # x = x +1
#     if x ==8:
#         break
#     elif x ==4:
#         continue
#
#     print(x)

############################################################
#
#
#                      Задачи                             #


# Задача-1: поработайте с переменными, создайте несколько,
# t1 = input('Введи что-нибудь: ')
# print(t1)
#
#
# Задача-2: Запросите от пользователя число, сохраните в переменную,
# t2 = int(t1)
# print(t2 + 10)
#
# Задача-3: Запросите у пользователя его возраст.
#t3 = int(input("Сколько лет?"))
# if t3 < 18:
#     print("Доступ закрыт")
# else:
#     print("Разрешено")
#---------------------------------------------------------------

# Задача: используя цикл запрашивайте у пользователя число пока оно не станет больше 0, но меньше 10.
# После того, как пользователь введет корректное число, возведите его в степерь 2 и выведите на экран.
#
# col = int(input('Введите число от 0 до 10: '))
#
# while col < 1 or col > 10:
#     print('Неправильно, повтори')
#     col = int(input('Введите число от 0 до 10: '))
#
# col = col ** 2
# print(col)
#---------------------------------------------------------------
# while True:
#     num = int(input('Введите число от 0 до 10: '))
#     if 0 < num <10:
#         print(num ** 2)
#         break
#     else:
#         print("Неверное число")
#---------------------------------------------------------------

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.

# a = int(input("Введите число a:"))
# b = int(input("Введите число b:"))
# a = b
# b = a
# print("Теперь а =", a)
# print("А b =", b)
#---------------------------------------------------------------

#HARD

name = input("Ваше имя: ")
sername = input("Фамилия: ")
age = int(input("Возраст: "))
weight = int(input("Вес: "))

# if age < 30:
#     if weight > 50 and weight < 120:
#         print(name, sername, ",", age, ",", weight, " - Все хорошо")
#     else:
#         print(name, sername, ",", age, ",", weight, " - Скоректируйте вес! для человека младше 30 это не очень!")
#
# elif age > 30 and age < 40:
#     if weight > 50 and weight < 120:
#         print(name, sername, ",", age, ",", weight, " - следует заняться собой")
#
#     else:
#         print(name, sername, ",", age, ",", weight,  " - Скоректируйте вес! для человека старше 30 это не очень!")
#
#
# elif age > 40:
#     if weight < 50 or weight > 120:
#         print(name, sername, ",", age, ",", weight, " - следует обратится к врачу!")
#     else:
#         print(name, sername, ",", age, ",", weight, " - следует заняться собой после 40")

#---------------------------------------------------------------

if age <= 30 and 50 <= weight <= 120:
    print('Все хорошо', name, age)
elif age >40 and (weight <50 or weight > 120):
    print('Вам бы к врачу', name, age)
elif age >30 and (weight < 50 or weight > 120):
    print('Вам бы спонртом заняться', name, age)
else:
    print('Не подходите под формулу')
