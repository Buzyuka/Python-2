import re
import csv
from itertools import groupby
from operator import itemgetter


def flat_map(lst):
    """
    Преобразование списка из списков в линеынй список.

    :param lst: Спискок из списков: [[A, B], [C, D], [E, F]]
    :return: Линейный список: [A, B, C, D, E, F]
    """
    return [y for x in lst for y in x]


def get_data(file_name):
    with open(file_name, "r") as f:
        text = f.read()

        os_prod = re.search(r"Изготовитель системы:[ ]*(.+)\n", text)
        os_name = re.search(r"Название ОС:[ ]*(.+)\n", text)
        os_code = re.search(r"Код продукта:[ ]*(.+)\n", text)
        os_type = re.search(r"Тип системы:[ ]*(.+)\n", text)

        assert (os_prod and os_name and os_code and os_type)

        return (
            ("Изготовитель системы", os_prod.group(1)),
            ("Название ОС", os_name.group(1)),
            ("Код продукта", os_code.group(1)),
            ("Тип системы", os_type.group(1)),
        )


def write_to_csv(data, file_name):
    flat_data = sorted(flat_map(data), key=itemgetter(0))
    grouped = groupby(flat_data, key=itemgetter(0))
    cvs_data = []

    for title, items in grouped:
        row = [title]
        row.extend(map(itemgetter(1), items))
        cvs_data.append(row)

    # Транспонирование матрицы
    cvs_data = zip(*cvs_data)
    _write_cvs_data(cvs_data, file_name)


def _write_cvs_data(rows, file_name):
    with open(file_name, "w") as f:
        writer = csv.writer(f)

        for row in rows:
            writer.writerow(row)


data = [
    get_data("info_1.txt"),
    get_data("info_2.txt"),
    get_data("info_3.txt"),
]

write_to_csv(data, "report.csv")
