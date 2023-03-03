# Задача 18: Требуется найти в массиве A[1..N]
# самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
#
# *Пример:*
#
# 5
#     1 2 3 4 5
#     6
#     -> 5

import  random


n = int(input('Введите кол-во элементов в массиве: '))
my_list = []
for i in range(n):
    my_list.append(random.randint(0,9))

my_list.append(n)
my_list.sort()
print(my_list)

x = int(input('Введите число от 0 до 9: '))
count = 0
for i in range(0,len(my_list)):
    if my_list[i] == x or my_list[i] < x < my_list[i+1]:
        count = my_list[i]
        break

print(f'Приближенный к числу {x} - {count}')