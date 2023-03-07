# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
import random

# создаем рандомный список

n = int(input("Введите n: "))
new_list = [random.randint(-10,10) for i in range(n)]
print(new_list)

# ограничение

max_value, min_value = int(input('Введите максимум: ')), int(input('Введите минимум: '))

count = []

for i in range(len(new_list)):
    if min_value < new_list[i] < max_value:
        count.append(i)

print(f'Индексы которые входит в  промежуток [{min_value}, {max_value}] = {count}')