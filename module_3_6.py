def calculate_structure_sum(*args): # recursive counting function
    global call_counter
    call_counter += 1
    result = 0
    for x in args:
        if isinstance(x, int):  # count all integers
            result += x
        elif isinstance(x, str):  # sum up the lengths of all strings
            result += len(x)
        elif isinstance(x, (list, tuple,
                            set)):  # recursively counting nested elements in lists, tuples and sets
            result += calculate_structure_sum(*x)
        elif isinstance(x, dict):  # recursively counting elements in a dictionary
            result += calculate_structure_sum(*tuple(x.items()))
    return result


call_counter = 0
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
print(f'{calculate_structure_sum(data_structure)} - это результат \nрекурсивного '
      f'подсчета\nвсевозможных чисел')
print(f'{call_counter} - вызовов функции')

consol:
# 99 - это результат 
# рекурсивного подсчета
# всевозможных чисел
# 16 - вызовов функции
