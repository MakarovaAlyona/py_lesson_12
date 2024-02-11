from data_create import name_data, surname_data, phone_data, address_data

def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input(f"В каком формате записать данные\n\n"
    f"1 Вариант:  \n"
    f"{name}\n{surname}\n{phone}\n{address}\n\n"
    f"2 Вариант:  \n"
    f"{name};{surname};{phone};{address}\n"
    f"Выберите вариант: "))

    while var != 1 and var !=2:
        print("Неправильный ввод")
        var = int(input("Введите число "))
    if var == 1:
        with open("d_first_var.csv", 'a', encoding='utf-8') as f:
             f.write(f"{name}\n{surname}\n{phone}\n{address}\n\n")
    elif var == 2:
        with open("d_second_var.csv", 'a', encoding='utf-8') as f:
             f.write(f"{name};{surname};{phone};{address}\n\n")
def print_data():
    print('Вывожу данные из 1 файла: \n')
    with open("d_first_var.csv", 'r', encoding='utf-8') as f:
        data_first = f.readlines()
        data_first_list = []
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first) - 1:
                data_first_list.append(''.join(data_first[j:i+1]))
                j = i
        print(''.join(data_first_list))
    print('Вывожу данные из 2 файла: \n')
    with open("d_second_var.csv", 'r', encoding='utf-8') as f:
        data_second = f.readlines
        print(*data_second)
        return data_second


def change_data():
    data_list = print_data()
    name_data_d = input('Введите данные, которые хотите изменить: ')
    number_file = int(input('Введите, из какого файла вы хотите внести изменения: '))
    while number_file != 1 and number_file != 2:
        print('Неправильный ввод')
        number_file = int(input('Введите, из какого файла вы хотите внести изменения: '))
    if number_file == 1:
        with open('d_first_var.csv', 'w', encoding='utf-8') as f:
            for i in range(len(data_list)):
                if str(data_list[i]).startswith(name_data_d):
                    for j in range(i):
                        f.write(data_list[j])
                    data_list[i] = input_data()
                    f.write(data_list[i])
                    for k in range(i + 5, len(data_list) - 1):
                        f.write(data_list[k])

    elif number_file == 2:
        with open('d_second_var.csv', 'w', encoding='utf-8') as f:
            for i in range(len(data_list)):
                if str(data_list[i]).startswith(name_data_d):
                    f.write(str(*data_list[:i]))
                    data_list[i] = input_data()
                    f.write(str(data_list[i]))
                    f.write(str(*data_list[i+1:]))


def delete_data():
    data_list = print_data()
    name_data_d = input('Введите имя данных котопые вы хотите удалить: ')
    number_file = int(input('Введите номер файла в котором вы хотите удалить данные: '))
    while number_file != 1 and number_file != 2:
        print('Неправильный ввод')
        number_file = int(input('Введите номер файла в котором вы хотите удалить данные: '))
    if number_file == 1:
        with open('d_first_var.csv', 'w', encoding='utf-8') as f:
            for i in range(len(data_list)):
                if str(data_list[i]).startswith(name_data_d):
                    for j in range(i):
                        f.write(data_list[j])
                    for k in range(i + 5, len(data_list) - 1):
                        f.write(data_list[k])
    elif number_file == 2:
        with open('d_second_var.csv', 'w', encoding='utf-8') as f:
            for i in range(len(data_list)):
                if str(data_list[i]).startswith(name_data_d):
                    f.write(str(*data_list[:i]))
                    f.write(str(*data_list[i + 1:]))


