# Напишите функцию sum_range(start, end), которая суммирует все целые числа от значения 
# start до величины end включительно.


def sum_range(start, end):
    return sum(range(start, end + 1))
result = sum_range(10, 20)
print('ChatGPT result = ', result)


