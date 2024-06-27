from data_create import name_data, surname_data, phone_data, address_data


def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input(f"В каком формате записать данные?\n\n"
                    f"1 Вариант: \n"
                    f"{name}\n{surname}\n{phone}\n{address}\n\n"
                    f"2 Вариант: \n"
                    f"{name};{surname};{phone};{address}\n"
                    f"Выберите вариант: "))

    while var != 1 and var != 2:
        print("Неправильный ввод")
        var = int(input("Введите число: "))

    if var == 1:
        with open('data_first_variant.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name}\n{surname}\n{phone}\n{address}\n\n")
    elif var == 2:
        with open('data_second_variant.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name};{surname};{phone};{address}\n")
    return var


def print_data():
    print("Вывожу данные из 1-ого файла: \n")
    with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
        data_first = f.readlines()
        data_first_list = []
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first) - 1:
                data_first_list.append(''.join(data_first[j:i + 1]))
                j = i
        data_first_list_final = []

        for i in range(len(data_first_list)):  # Удаляем дублирующиеся переносы строк в списке
            if data_first_list[i] != '\n\n':
                data_first_list_final.append(data_first_list[i])
        print(''.join(data_first_list_final))

    print("Вывожу данные из 2-ого файла: \n")
    with open('data_second_variant.csv', 'r', encoding='utf-8') as f:
        data_second = f.readlines()
        print(*data_second, sep='')


def change_data():
    k = int(input("Введите номер записи, который Вы хотите изменить: "))
    var = input_data()  # Вызываем функцию input_data(), которая добавляет запись в конец файла,
    # а также возвращает значение переменной var
    if var == 1:
        with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
            data_first = f.readlines()
        data_first_list = []
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first) - 1:
                data_first_list.append(''.join(data_first[j:i + 1]))
                j = i
        data_first_list_final = []

        for i in range(len(data_first_list)):  # Удаляем дублирующиеся переносы строк в списке
            if data_first_list[i] != '\n\n':
                data_first_list_final.append(data_first_list[i])
        print(data_first_list_final)

        change_line = data_first_list_final.pop()  # Извлекаем последнюю запись (элемент) из списка
        # и сохраняем в переменную change_line
        data_first_list2 = data_first_list_final[:k - 1] + [change_line] + data_first_list_final[k:]

        with open('data_first_variant.csv', 'w', encoding='utf-8') as f:
            f.writelines(data_first_list2)

    elif var == 2:
        with open('data_second_variant.csv', 'r', encoding='utf-8') as f:
            data_second = f.readlines()
            change_line = data_second.pop()
            data_second_list = data_second[:k - 1] + [change_line] + data_second[k:]
        with open('data_second_variant.csv', 'w', encoding='utf-8') as f:
            f.writelines(data_second_list)


def remove_data():
    var = int(input(f"В каком файле удалить запись?\n\n"
                    f"1 Вариант (Файл 'data_first_variant.csv'): \n"
                    f"{'name'}\n{'surname'}\n{'phone'}\n{'address'}\n\n"
                    f"2 Вариант (Файл 'data_second_variant.csv'): \n"
                    f"{'name'};{'surname'};{'phone'};{'address'}\n"
                    f"Выберите вариант: "))

    while var != 1 and var != 2:
        print("Неправильный ввод")
        var = int(input("Введите число: "))

    n = int(input("\n Какую запись вы хотите удалить? \n Введите номер записи: "))
    if var == 1:
        with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
            data_first = f.readlines()
            j = 0
            data_first_list = []
            for i in range(len(data_first)):
                if data_first[i] == '\n' or i == len(data_first) - 1:
                    data_first_list.append(''.join(data_first[j:i + 1]))
                    j = i
            data_first_list_final = []
            for i in range(len(data_first_list)):  # Удаляем дублирующиеся переносы строк в списке
                if data_first_list[i] != '\n\n':
                    data_first_list_final.append(data_first_list[i])
            data_first_list2 = data_first_list_final[:n - 1] + data_first_list_final[n:]
        with open('data_first_variant.csv', 'w', encoding='utf-8') as f:
            f.writelines(data_first_list2)
    elif var == 2:
        with open('data_second_variant.csv', 'r', encoding='utf-8') as f:
            data_second = f.readlines()
            data_second_list = data_second[:n - 1] + data_second[n:]
        with open('data_second_variant.csv', 'w', encoding='utf-8') as f:
            f.writelines(data_second_list)