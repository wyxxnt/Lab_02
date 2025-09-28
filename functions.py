def average(a, b):
    result = (a + b) / 2
    return result

def square(x):
    result = x * x
    return result

def cube(x):
    result = x * x * x
    return result

def calculate():
    results = []
    for i in range(0, 10):
        sq = square(i)
        cb = cube(i)
        avg = average(sq, cb)
        results.append(avg)
    return results

calc_results = calculate()
print('Результати обчислень:', calc_results)
