# Задача 2. Всё в одном

import os

list_path = list()


def copy_file(destination_path, files_path_list):
    write_file = open(os.path.join(destination_path, 'new_copy_all_files.txt'), 'a')
    for file in files_path_list:

        read_file = open(file, 'r')
        write_file.write(read_file.read())
        write_file.write('\n')
        write_file.write('*' * 40)
        write_file.write('\n')
        read_file.close()
    write_file.close()


def find_file(user_path, list_way):
    for element in os.listdir(user_path):
        path = os.path.join(user_path, element)
        if os.path.isfile(path):
            if path.endswith('.py'):
                list_way.append(path)
        else:
            find_file(path, list_way)


user_read_path = input('Введите имя каталога из которого будет осуществляться поиск и копирование файлов: ')
user_write_file_path = input('Введите путь по которому будет сохранен результирующий файл: ')

find_file(user_read_path, list_path)
copy_file(user_write_file_path, list_path)
