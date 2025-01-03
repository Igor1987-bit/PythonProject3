# Функция count_calls - количество всех других функций, кроме count_calls
def count_calls():
    global calls
    calls += 1
# Функция длины переданной строки, строка.upper(), строка.lower()
def string_info(string):
    count_calls()
    return (len(string), string.upper(), string.lower())
# Функция проверки наличия строки в списке независимо от регистра
def is_contains(string, list_to_search):
    count_calls()
    list_to_search = [i.lower() for i in list_to_search]  # весь список в нижний регистр
    return (string.lower() in                             # строка тоже в нижний регистр
            [j for j in list_to_search])
# Вывод результатов
calls = 0
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)
# consol
# (8, 'CAPYBARA', 'capybara')
# (10, 'ARMAGEDDON', 'armageddon')
# True
# False
# 4
