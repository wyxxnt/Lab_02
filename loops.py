def range_func(start, end):
    result = []
    for i in range(start, end + 1):
        result.append(i)
    return result

def range_odd(start, end):
    result = []
    for i in range(start, end + 1):
        if i % 2 == 1:
            result.append(i)
    return result

numbers = range_func(15, 30)
print('Діапазон чисел:', numbers)

odd_numbers = range_odd(15, 30)
print('Непарні числа:', odd_numbers)
