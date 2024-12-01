# Написать функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения 
# (с помощью кортежа, после return перечислить все значения через запятую): периметр квадрата, 
# площадь квадрата и диагональ квадрата.


import math as m

def square_with_arg(l):
    result_1 = l * 4    # периметр
    result_2 = l ** 2   # площадь квадрата
    result_3 = l * m.sqrt(2)   # диагональ квадрата
    return result_1, result_2, result_3

l = 5
result = square_with_arg(l)
print (result[0], "периметр")
print (result[1], "площадь квадрата")
print (result[2], "диагональ")
print()
print(f"Периметр: {result[0]}, Площадь: {result[1]}, Диагональ: {result[2]:}")