# Задача 2. Всё в одном

import os

list_path = list()


def copy_file(file_path, destination_path):
    use_file = open('file_path', 'r')
    dest_file = open(os.path.join(destination_path, 'new_copy_all_files.txt'), 'a')
    for line in use_file:
        dest_file.write(line)
    dest_file.write('\n')
    dest_file.write('*' * 40)
    use_file.close()
    dest_file.close()


def find_file(user_path, list_way):
    for element in os.listdir(user_path):
        path = os.path.join(user_path, element)
        if os.path.isfile(path):
            list_way.append(path)
        else:
            find_file(path, list_way)


user_read_path = input('Введите имя каталога из которого будет осуществляться поиск и копирование файлов: ')
user_write_file_path = input('Введите путь по которому будет сохранен результирующий файл: ')

find_file(user_read_path, list_path)

for line in list_path:
    copy_file(line, user_write_file_path)