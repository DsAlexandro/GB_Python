# Задача 2: Найдите сумму цифр трехзначного числа.
#
# *Пример:*
#
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

number = int(input('Введите трёхзначного число: '))

if number // 100 < 9 and number // 10 > 10:
    summa = number // 100 + number % 10 + number % 100 // 10
    print(f'Сумма трехзначного числа = {summa}')
else:
    print('Вы ввели неккоректное число!!!')