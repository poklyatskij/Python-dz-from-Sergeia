# Погружение в Python (лекции)
# Урок 4. Функции

"""
Функции высшего порядка
Фунцией высшего порядка называется такая функция, которая принимает функцию объект как 
аргумент или возвращает функцию объекта в виде выходного значения.

Функция вызывает
print(42)

Функция передаёт
func = cum

"""
# a = 42
# print(type(a), id(a))
# print(type(id))


# ver_bad_programming_style = sum
# print(ver_bad_programming_style([1, 2, 3]))


"""
Определение собственной функции

Зарезервированное слово def
"""

# def my_func():
#     pass


"""
Что такое pass?

Зарезервированное слово pass ничего не делает

Плохо

if a != 5:
    pass
else:
    a += 1


Лучше

if a == 5:
    a += 1
else:
    pass


Отлично

if a == 5:
    a += 1

"""


"""
Аргументы функции

После имени функции в круглых скобках 
указываются параметры функции через запятую

def qadratic_equations(a, b, c):
"""

# def qadratic_equations(a: int | float, b: int | float, c: int | float,) -> tuple[float, float] | float | str:
#     d = b ** 2 - 4 * a * c
#     if d > 0:
#         return (-b * d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a)
#     elif d == 0:
#         return -b / (2 * a)
#     else:
#         return 'Нет решений'


# print(qadratic_equations(2, -3, -9))


"""
Изменяемые и не изменяемые аргументы

При передачи аргументов в функцию стоит помнить изменяемого типа объект или нет.

Не изменяемый аргумент 

При изменении в нутри функции остается прежним в ней функция.

Изменяемый аргумент

При изменении в нутри функции изменяется и за её пределами.


В Python аргументы передаются в нутри функции по ссылке на объект!
"""

# def no_mutable(a: int) -> int:
#     a += 1
#     print(f'In fonc {a = }') # для демонстрации работы, но не для привычки принтить из функции
#     return a


# a = 42
# print(f'In main {a = }')
# z = no_mutable(a)
# print(f'{a = }\t{z = }')


# def mutable(data: list[int]) -> list[int]:
#     for i, item in enumerate(data):
#         data[i] = item + 1
#     print(f'In func {data = }') # для демонстрации работы, но не для привычки принтить из функции
#     return data


# my_lisl = [2, 4, 6, 8]
# print(f'In main {my_lisl = }')
# new_list = mutable(my_lisl)
# print(f'{my_lisl = }\t{new_list = }')


"""
Возврат значения из функции, return

Если указан один объект после return
возвращается именно этот объект

Если указанно несколько значений черег запятую после return
возвращается кортеж с перечисленными значениями

Если ничего не указанно после return
возвращается None

Если return отсуцтвует
python "Мысленно" дописывает в качестве последней строки функции return None

"""


# def qadratic_equations(a, b, c):
#     d = b ** 2 - 4 * a * c
#     if d > 0:
#         return (-b * d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a)
#     if d == 0:
#         return -b / (2 * a)
#     else:
#         return None


# print(qadratic_equations(2, -3, -9))


"""
Значение по умолчанию

После параметра указываем значение по умолчанию

def qadratic_equations(a, b=0, c=0):

В качестве значения по умолчанию нельзя указывать изменяемые типы:
списки, словари, множества.
"""

# def qadratic_equations(a, b=0, c=0):
#     d = b ** 2 - 4 * a * c
#     if d > 0:
#         return (-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a)
#     if d == 0:
#         return -b / (2 * a)


# print(qadratic_equations(2, -9))


# def from_one_to_n(n, data=[]):
#     for i in range(1, n + 1):
#         data.append(i)
#     return data


# def from_one_to_n(n, data=None):
#     if data is None:
#         data = []
#     for i in range(1, n + 1):
#         data.append(i)
#     return data


# new_list = from_one_to_n(5)
# print(f'{new_list = }')
# other_list = from_one_to_n(7)
# print(f'{other_list = }')


"""
Позиционные и ключевые параметры

Косая черта / и звёздочка * разделяют позиционные и ключевые параметры

def func(positional_only, /, positional_or_keyword, *, keyword_only):
    pass
"""


# def tunc(positional_only_parameters, /, positional_or_keyword_parameters, *, keyword_only_parameters):
#     pass


# def standart_arg(arg):
#     """Пример обычной функции"""
#     print(arg) # Принтим для приёмаЮ а не для привычки


# def standart_arg(arg, /):
#     """Пример только позиционной функции"""
#     print(arg) # Принтим для приёмаЮ а не для привычки


# def standart_arg(*, arg):
#     """Пример только позиционной функции"""
#     print(arg) # Принтим для приёмаЮ а не для привычки


# standart_arg(42)
# standart_arg(arg=42)


# def combinet_example(pos_only, /, standard, *, kwd_only):
#     """Пример функции со всеми вариантами параметров"""
#     print(pos_only, standard, kwd_only) # Принтим для примера, а не для привычки


# combinet_example(1, 2, kwd_only=3)
# combinet_example(1, standard=2, kwd_only=3)
# combinet_example(pos_only=1, standard=2, kwd_only=3)


"""
Параметры *args и **kwargs

Именна args и kwargs - бще принятое соглашение

def func(*args): - принимает любое число позиционных аргументов.

def func(**kwards): - принимает любое число ключевых аргументов.

def func(*args, **kwards): - принимает любое число позиционных и ключевых аргументов.

"""

# def mean(args):
#     return sum(args) / len(args)


# print(mean([1, 2, 3]))
# # print(mean(1, 2, 3)) # TypeError: mean() takes 1 positional argument but 3 were given


# def mean(*args):
#     return sum(args) / len(args)


# print(mean(*[1, 2, 3]))
# print(mean(1, 2, 3))


# def school_print(**kwards):
#     for key, value in kwards.items():
#         print(f'По предмету "{key}" полученна оценка {value}')


# school_print(химия=5, физика=4, математика=5, физра=5)


"""
Области видимости

Локальная
код внутри самой функции, т.е, переменные заданные в теле функции.

Глобальная, global
код модуля, т.е, переменные заданные в файле py содержащие функцию.

Не локальная, nonlocal
код внешней функции, исключающий доступ к глобальным переменным.

Доступ к глобальной КОНСТАНТЕ из тела функции - нормально.

"""

"""Локальные переменные"""


# def func(y: int) -> int:
#     x = 100
#     #x += 100
#     print(f'In func {x = }')
#     return y + 1


# def func(y: int) -> int:
#     """Глобальные переменные"""
#     global x
#     x += 100
#     print(f'In func {x = }')
#     return y + 1


# def main(a):
#     """Не локальные переменные"""
#     x = 1

#     def func(y):
#         nonlocal x
#         x += 100
#         print(f'In func {x = }')
#         return y + 1

#     return x + func(a)


# x = 42
# print(f'In func {x = }')
# z = main(x)
# print(f'In func {x = }\t{z = }')

LIMIT = 1_000


def func(x, y):
    result = x ** y % LIMIT
    return result


print(func(42, 73))


"""
Анонимная функция lambda

lambda parameters: action

Анонимная функция, они же lambda функции - синтаксический сахар для 
обычных питоновских функций с рядом ограничений. Они позволяют задать функцию в одну строку
кода без использования других ключевых слов.
"""


def add_two_def(a, b):
    return a + b


add_two_lambda = lambda a, b: a + b

print(add_two_def(42, 3.14))
print(add_two_lambda(42, 3.14))


my_dict = {'two': 2, 'one': 1, 'four': 4, 'three': 3, 'ten': 10}
s_key = sorted(my_dict.items())
s_value = sorted(my_dict.items(), key=lambda x: x[1])
print(f'{s_key = }\n{s_value = }')


"""Документирование кода функции"""

def max_before_hundred(*args):
    """Return the maxsimum number not exceeging 100.
    
    :param args: tuple of int or float numbers
    :return: int or float number from the tuple args
    """
    m = float('-inf')
    for item in args:
        if m < item < 100:
            m = item
    return m


print(max_before_hundred(-42, 73, 256, 0))
help(max_before_hundred)


"""
Встроенные функции

В python есть ряд встроенных функций. Перечислим их в алфовитном порядке:
abs(), aiter(), all(), any(), anext(), ascii(), bin(), bool(), breakpoint(),
bytearray(), bytes(), callable(), chr(), classmethod(), compile(), complex(),
delattr(), dict(), dir(), divmod(), enumerate(), tval(), exec(), filter(), float(),
format(), frozenset(), detattr(), globals(), hasattr(), hasah(), help(),
hex(), id(), input(), int(), isinstance(), issubclass(), iter(), len(), list(),
locals(), map(), max(), memjryview(), min(), next(), object(), oct(), open(),
ord(), pow(), print(), property(), gange(), repr(), reversed()

"""









