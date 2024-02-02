# 2. Напишите функцию группового переименования файлов. Она должна:
# a. принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# b. принимать параметр количество цифр в порядковом номере.
# c. принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
# d. принимать параметр расширение конечного файла.
# e. принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из
# исходного имени файла. К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.

import os
from pathlib import Path


def rename_f(directory: str, part_start_name: tuple[int,int] = (None,None),\
             name_f: str = '', ext_start: str = '', ext_finish: str = '', num_num: int = 2) -> None:
    """ Function renames files with options

    :param directory: str Work folder
    :param part_start_name: tuple which sets interval of original name
    :param name_f: str new file name
    :param ext_start: str original file extention
    :param ext_finish: str new file extention
    :param num_num: int number of digits
    :return: None
    """
    list_file = []
    n_dir = Path(directory)

    # Делаем список только файлов с расширением ext_start если оно задано
    for item in n_dir.iterdir():
        if item.is_file() is True and ext_start == '':
            list_file.append(item)
        if item.is_file() is True and str(item).split('.')[1] == ext_start:
            list_file.append(item)
    a,b = part_start_name

    for num in range(len(list_file)):
        num_name = '' if num_num == 0 else '0'*(num_num - len(str(num))) + str(num)
        ext_name = f'{ext_finish}' if ext_finish != '' else str(list_file[num]).split('.')[1]
        new_name = str(list_file[num]).split("\\")[-1].split(".")[0][a:b] + name_f
        full_name = directory + '\\' + new_name + num_name + '.' + ext_name
        Path(list_file[num]).rename(full_name)

if __name__ == '__main__':
    print(rename_f(r"d:\my doc\Обучение\Бизнесс аналитик\20_погружение в Python\Lesson7\Test", name_f = 'test', ext_start='txxt', ext_finish='txxt'))
    # print(rename_f(Path.cwd(), name_f= 'test'))

