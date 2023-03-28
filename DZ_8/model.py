import variables
from prettytable import PrettyTable

user_list = []


def add_user():
    """Добавление пользователя"""
    while True:
        variables.line()
        if variables.ans() == 'д':
            variables.line()
            user_list.append(variables.new_user())
        else:
            variables.line()
            break

    with open('data_users.txt', 'a', encoding='utf-8') as du:
        # for i in enumerate(user_list):
        #     du.write(f'{i[0]}: {i[1]} \n')
        for i in range(len(user_list)):
            du.write(f'{user_list[i]}\n')


def show_users():
    """Показать пользователей"""
    file = open('data_users.txt', encoding='utf-8')
    print(file.read())
    file.close()


def delete_users():
    """Удаление пользователя"""

    file = open('data_users.txt', 'r', encoding='utf-8')
    delete_users = input('Кого удаляем? \n'
                         'Введите ФИО, если не помните полностью ФИО, нажмите "f" \n- ')
    if delete_users == 'f':
        find_user()
        delete_users = input('Кого удаляем? \n- ')
    user_list = file.readlines()
    user_list.remove(f'{delete_users}\n')
    file.close()
    with open('data_users.txt', 'w', encoding='utf-8') as du:
    #     for i in enumerate(user_list):
    #         du.write(f'{i[0]}: {i[1]}')
        for i in range(len(user_list)):
            du.write(f'{user_list[i]}')


def find_user():
    """Нахождение пользователя"""
    file = open('data_users.txt', encoding='utf-8')
    find_user = input('Кого ищем? \n- ')
    user_list = file.readlines()
    for i in range(len(user_list)):
        if find_user in user_list[i]:
            print('*' * len(user_list[i]))
            print(f'{user_list[i]}' + '*' * len(user_list[i]))


def replace_user():
    """Замена пользователя"""
    old = input('Введите кого нужно заменить - ')
    new = input('Введите ФИО нового участника - ')
    file = open('data_users.txt', encoding='utf-8')
    data = file.read()
    data = data.replace(old, new)
    file.close()
    file = open('data_users.txt', 'w', encoding='utf-8')
    file.write(data)
    file.close()