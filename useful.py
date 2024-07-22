from string import *

# Три варианта создания алфавита для 36-ой системы счисления (или меньше)
alphabet0 = '0123456789' + ascii_uppercase
alphabet1 = digits + ascii_uppercase
alphabet2 = sorted('012456789QWERTYUIOPASDFGHJKLZXCVBNM')


def my_convert(number: int, system: int) -> str:
    """
    Универсальная функция для перевода в системы счисления от 2-ой до 36-ой
    :param number: Переводимое 10-ное число
    :param system: Система счисления в которую будем переводить
    :return: Результат вернем в виде строки
    """
    alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
    result = ''
    while number > 0:
        result += alphabet[number % system]
        number //= system
    return result[::-1]


# Вызов функции my_convert:
n = int(input())  # Допустим введем: 8
b = int(input())  # Допустим введем: 2
print(my_convert(n, b))  # Получим: 1000


def my_int(num: list, base: int) -> int:
    """
    Универсальная функция перевода из base системы в 10-ю, используется при очень больших (>36) системах.
    :param num: Число в base системе счисления в виде списка
    :param base: Система счисления в которой находится число
    :return: Возвращает рпезультат в виде целого числа
    """
    return sum([x*base**i for i, x in enumerate(num[::-1])])


# Вызов функции my_int:
print(my_int([1, 0, 0, 0], 2))  # 8


def divisors(num: int) -> list:
    '''
    Функция поиска делителей числа num
    :param num: Принимает целое (int) число.
    :return: Возвращает список делителей от 1 до числа num
    '''
    res = []
    for j in range(1, int(num**0.5) + 1):
        if num % j == 0:
            res += [j, num // j]
            # res.append(j)
            # res.append(num // j)
    return sorted(set(res))


# Вызов функции divisors:
n = int(input())  # Допустим число 24
print(divisors(n))  # [1, 2, 3, 4, 6, 8, 12, 24]


def prime(x):
    """
    Функция проверяющая является ли число простым
    :param x: Принимает на вход целочисленное int число
    :return: Возвращает значение True, если число простое и False, если составное
    """
    if x == 1:
        return False
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True


# Вызов функции prime:
n = int(input())
if prime(n):
    print('Число простое!')
else:
    print('Число составное.')


def sum_of_string(my_str):
    """
    Функция поиска суммы цифр строки.
    :param my_str: Принимает на вход строку символов
    :return: Возвращает целочисленное значение int
    """
    summa = 0
    for x in my_str:
        if x.isdigit():
            summa += int(x)
    return summa


# Вызов функции sum_of_string:
s = input()
summa0 = sum_of_string(s)

# Другие вариации написания:
summa1 = sum([int(x) for x in s])
summa2 = sum([int(x) for x in s if x.isdigit()])
summa3 = sum(map(int, s))
# summa4 = s.count('1') + s.count('2') * 2 + ...


if __name__ == '__main__':
    print("Hello, world!")
