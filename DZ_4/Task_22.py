# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.

import random

import setuptools.command.bdist_egg

set_n = set()
set_m = set()

# создание множеств

n = int(input('Введите кол-во элементов первого множества - '))
for i in range(n):
    # set_n.add(random.randint(0,20))
    x = int(input('Введите элемент множества: '))
    set_n.add(x)

m = int(input('Введите кол-во элементов второго множества - '))
for i in range(m):
    # set_m.add(random.randint(0, 20))
    x = int(input('Введите элемент множества: '))
    set_m.add(x)

print(f'Первое множество: {set_n}')
print(f'Второе множество: {set_m}')

# нахождение повторяющих элементов

set_end = set.intersection(set_m,set_n)
set_end = list(set_end)
set_end.sort()

print(f'Объединение множеств: {set_end}')






