# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных.


def new_str():
    with open('phone_book.txt', 'a') as file:
        file.write(input('Введите новую строку' + '\n')+ '\n')


def show_book():
    with open('phone_book.txt', 'r') as file:
        book = file.read()
    return book


def Del(X):
    with open("phone_book.txt", "r") as f:
        lines = f.readlines()
    with open("phone_book.txt", "w") as f:
        for line in lines:
            if X not in line.strip("\n"):
                f.write(line)
            else: print(f"Удалили строку: {line}")
    return lines

def find(X):
    b = True
    with open("phone_book.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            if X in line.strip("\n"):
                print(line, end='')
                b = False
    if b: print("По Вашему запросу ничего не найдено, попробуйте изменить запрос")
    return lines



def change_person(new_name, old_name):
    with open("phone_book.txt", "r") as f:
        lines = f.readlines()
    with open("phone_book.txt", "w") as f:
        for line in lines:
            if old_name not in line.strip("\n"):
                f.write(line)
            else:
                print(f'Заменили строчку \n {line} на: \n {new_name}')
                f.write(new_name+'\n')
    return lines



while True:
    mode = input('Выберите режим работы справочника'+ '\n'
                 + '0-добавление записи, 1-чтение файла, 2-удаление, 3-поиск, 4-замена, 5-выход: ')
    if mode == '0':
        new_str()
    elif mode == '1':
        print(show_book())
    elif mode == '2':
        name = input('кого удаляем?: ')
        Del(name)
    elif mode == '3':
        name = input('что ищем?: ')
        find(name)
    elif mode == '4':
        old_name = input('Какую строчку изменить?: ')
        new_name = input('Введите строчку заново: ')
        change_person(new_name, old_name)
    elif mode == '5':
        break
    else:
        print('Введите номер режима заново!')