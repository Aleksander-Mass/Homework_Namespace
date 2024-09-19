# Создать переменную calls = 0 вне функций.
calls = 0

# Функция count_calls подсчитывающая вызовы остальных функций.
def count_calls():
    global calls
    calls += 1

#Функция string_info принимает аргумент - строку и возвращает кортеж из:
# длины этой строки, строку в верхнем регистре, строку в нижнем регистре.

def string_info(string):
    count_calls()  # Увеличиваем счетчик вызовов
    return (len(string), string.upper(), string.lower())



#Функция is_contains принимает два аргумента: строку и список, и возвращает True,
# если строка находится в этом списке, False - если отсутствует.
# Регистром строки при проверке пренебречь: UrbaN ~ URBAN.
#Создать функцию is_contains с двумя параметрами string и list_to_search,

def is_contains(string, list_to_search):
    count_calls()  # Увеличиваем счетчик вызовов
    string = string.lower()  # Приводим строку к нижнему регистру
    list_to_search = [item.lower() for item in list_to_search]  # Приводим список к нижнему регистру
    return string in list_to_search


# Пример вызовов функций
print(string_info('Homework'))
print(string_info('PraCTical'))
print(string_info('Operators'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Должен вернуть True
print(is_contains('cycle', ['recycling', 'cyclic']))    # Должен вернуть False
print(is_contains('Namespase', ['Spase', 'Function', 'nAmEsPaSe']))

# Вывод значения глобальной переменной calls
print(calls)

"""
Вывод на консоль:
(8, 'HOMEWORK', 'homework')
(9, 'PRACTICAL', 'practical')
(9, 'OPERATORS', 'operators')
True
False
True
6
"""