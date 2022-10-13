# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов
# (от 0 до 10) многочлена,
# записать в файл полученный многочлен не менее 3-х раз.

from random import randint, choice


def get_string(num: int):
    line = ""
    signs = ['+ ', '- ']
    while num:
        occ = randint(0, 10)
        if occ:
            line += f'{occ}*x^{num} '
            line += choice(signs)
        num -= 1
    line += f"{randint(0, 10)} = 0\n"
    return line


number = int(input("введите число: "))
with open("equations.txt", "a", encoding="utf-8") as file:
    if number > 0:
        file.write(get_string(number))