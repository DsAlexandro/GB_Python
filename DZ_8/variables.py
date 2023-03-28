# Файл для хранение переменных

def new_user():
    """Создание нового пользователя"""
    second_user = input('Введите фамилию - ')
    first_user = input('Введите имя - ')
    user = input('Введите отчество - ')
    fio = second_user + ' ' + first_user + ' ' + user
    # number = input('Введите номер телефона ')
    return fio
def line():
    """Просто линия"""
    line = print('---------------------------------------------')
    return line


def ans():
    """Продолжение"""
    ans = input('Хотите добавить ещё одного пользователя? (д/н)')
    return ans
