# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, \
# и возводит число А в целую степень B с помощью рекурсии.
#
# *Пример:*
#
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8

a = int(input("Введите А: "))
b = int(input("Введите В: "))


def sqr(a, b):
    if a > 0 and b == 0:
        a = 1
        return a
    elif b == 1:
        return a
    elif b > 0:
        return a * sqr(a, b - 1)
    elif b < 0:
        return 1 / a * sqr(a, b + 1)


if a == 0 and b < 0:
    print('Число ноль невозможно возвести в отрицательную степень!! ')
else:
    print(f'Число "{a}" в степении "{b}" = {sqr(a, b)}')
