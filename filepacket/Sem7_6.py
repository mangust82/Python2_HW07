# Дорабатываем функции из предыдущих задач.
# Генерируйте файлы в указанную директорию — отдельный параметр функции.
# Отсутствие/наличие директории не должно вызывать ошибок в работе функции (добавьте проверки).
# Существующие файлы не должны удаляться/изменяться в случае совпадения имён.

from random import choices, randint, randbytes
from string import ascii_lowercase, digits
from pathlib import Path
import os


def gen_files(ext: str, min_name: int = 6, max_name: int = 30, min_size: int = 256,
              max_size: int = 4096, file_count: int = 42) -> None:
    for _ in range(file_count):
        while True:
            name = ''.join(choices(ascii_lowercase + digits + '_', k=randint(min_name, max_name)))
            if not Path(f'{name}.{ext}').is_file():
                break
        data = bytes(randint(0, 255) for _ in range(randint(min_size, max_size)))
        with open(f'{name}.{ext}', 'wb') as f:
            f.write(data)



def gen_different_files(directory: Path, **kwargs) -> None:
    if isinstance(directory, str):
        directory = Path(directory)
    if not directory.is_dir():
        directory.mkdir(parents=True)
    os.chdir(directory)
    for ext, numbers in kwargs.items():
        gen_files(ext, file_count=numbers)


if __name__ == '__main__':
    gen_different_files(r"C:\Users\77017\PycharmProjects\python_data_seminar_7\test\spam", txt=2, doc=4, bin=3)

