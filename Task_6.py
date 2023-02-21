# Задача 6: Вы пользуетесь общественным транспортом?
# Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая
# проверяет счастливость билета.
#
# *Пример:*
#
# 385916 -> yes
# 123456 -> no


number = int(input('Введите номер с билета: '))



if number // 100000 < 9 and number // 10000 > 10:
    left_number = number % 1000
    left_number = left_number // 100 + left_number % 10 + left_number % 100 // 10
    right_number = number // 1000
    right_number = right_number // 100 + right_number % 10 + right_number % 100 // 10
    if right_number == left_number:
        print('You are lucky!!')
    else:
        print('Upps')
else:
    print('Странный билет, посмотрите внимательно и введите номер с билета ещё раз!')