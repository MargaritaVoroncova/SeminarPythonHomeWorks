# 5. ** Даны два файла, в каждом из которых находится запись многочленов. 
# Задача - сформировать файл, содержащий сумму многочленов.
from random import choice


def poly_sum(name_1: str, name_2: str):
    with open(name_1, "r", encoding="utf-8") as my_f_1, \
            open(name_2, "r", encoding="utf-8") as my_f_2:
        first = my_f_1.readlines()
        second = my_f_2.readlines()

        if len(first) == len(second): # проверка на совпадение количества строк в файлах
            with open("sum_poly.txt", "a", encoding="utf-8") as my_f_3:
                for i, v in enumerate(first): # enumerate возвращает кортеж, содержащий отсчет от start и значение, полученное из итерации
                    my_f_3.write(f"{v[:-5]} + {second[i]}") # удаляем с его помощью последние 5 элементов из строки первого файла (= пробел 0 /n)
        else:
            print("The contents of the files do not match!")
