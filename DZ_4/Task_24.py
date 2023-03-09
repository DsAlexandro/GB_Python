# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику.
# Она растет на круглой грядке, причем кусты высажены только по окружности. Таким образом, у каждого куста есть ровно
# два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод –
# на i-ом кусте выросло ai ягод.В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход, находясь
# непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
#
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий
# модуль, находясь перед некоторым кустом заданной во входном файле грядки.
import random

# создаем кол-во кустов и урожайнойсть каждого куста
n = int(input('Введите количество кустов: '))
bed_list = []

for i in range(n):
    x = random.randint(1,10)
    bed_list.append(x)

print(bed_list)

# Считаем максимальное количество ягод
count = []
for i in range(n-1):
    count.append(bed_list[i-1] + bed_list[i] + bed_list[i+1])

count.append(bed_list[-2] + bed_list[-1] + bed_list[0])
print(count)

print(max(count))

