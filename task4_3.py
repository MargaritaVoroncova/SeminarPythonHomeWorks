# Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности в том же порядке.
# in 7
# out
# [4, 5, 3, 3, 4, 1, 2]
# [5, 1, 2]
from random import randint


def get_random_int_list(size: int) -> list:
    if size < 0:
        print("Negative value of the number of numbers!")
        return []
    array = []
    for i in range(size):
        array.append(randint(1, 9))
    return array


def unique_values_list(some_list: list) -> list:
    array = []
    for i in some_list:
        if some_list.count(i) == 1:
            array.append(i)
    return array


num = int(input("Input integer number: "))
lst = get_random_int_list(num)
print(lst, unique_values_list(lst), sep="\n")