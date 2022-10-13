# Вычислить число c заданной точностью d

from decimal import Decimal

num = Decimal(input('Введите любое число: '))
acc = Decimal(input("До какого знака округлить? Например: '0.0001': "))

print(num.quantize(acc, "ROUND_HALF_UP"))