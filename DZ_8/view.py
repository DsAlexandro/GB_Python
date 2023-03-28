# Модуль взаимодействие с пользователем
import model
import variables

# Меню

def menu():
    """Выбор действия пользователя  """

    while True:
        menu = int(input('1: Создать пользователя \n2: Найти пользователя \n'
                         '3: Посмотреть телефонный справочник \n'
                         '4: Удалить пользователя \n'
                         '5: Заменить пользователя \n'
                         '6: Закрыть справочник\n'
                         'Ваш выбор: '))
        if menu == 1:
            model.add_user()
        elif menu == 2:
            variables.line()
            model.find_user()
            variables.line()
        elif menu == 3:
            variables.line()
            model.show_users()
            variables.line()
        elif menu == 4:
            variables.line()
            model.delete_users()
            variables.line()
        elif menu == 5:
            variables.line()
            model.replace_user()
            model.show_users()
            variables.line()
        elif menu == 6:
            break