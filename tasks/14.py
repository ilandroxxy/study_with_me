
# region 📚 Шпаргалка ЕГЭ | Задание №14

# Задание №1:
# Значение арифметического выражения 3 ∙ 625^173 + 4 ∙ 125^180 + 3 ∙ 25^157 + 2 ∙ 5^155 + 156
# записали в системе счисления с основанием 25.
# Сколько значащих нулей содержится в этой записи?

# Решение:
'''
def my_convert(number: int, system: int) -> str:
    alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
    result = ''
    while number > 0:
        result += alphabet[number % system]
        number //= system
    return result[::-1]

x = 3 * 625 ** 173 + 4 * 125 ** 180 + 3 * 25 ** 157 + 2 * 5 ** 155 + 156
s = my_convert(x, 25)
print(s.count('0'))
'''


# Задание №2:
# Операнды арифметического выражения записаны в системе счисления с основанием 15.
#
# 1x51_15 − 3x2_15
#
# В записи чисел переменной x обозначена неизвестная цифра из алфавита 15-ричной системы счисления.
# Определите наибольшее значение x, при котором значение данного выражения кратно 4.
# Для найденного x вычислите частное от деления данного выражения на 4 и запишите его
# в ответе в десятичной системе счисления. Основание системы счисления указывать не нужно.

# Решение:
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
M = []
for x in alphabet[:15]:
    A = int(f'1{x}51', 15)
    B = int(f'3{x}2', 15)
    if (A - B) % 4 == 0:
        M.append((A - B) // 4)
print(max(M))
'''


# Задание №3:
# Операнды арифметического выражения записаны в системах счисления с основаниями 9 и 8:
#
# x01y4_9 + xy544_8
#
# В записи чисел переменными x и y обозначены допустимые в данных системах счисления неизвестные цифры.
# Определите значения x и y, при которых значение данного арифметического выражения будет наименьшим и кратно 89.
# Для найденных значений x и y вычислите частное от деления значения арифметического выражения на 89
# и укажите его в ответе в десятичной системе счисления. Основание системы счисления в ответе указывать не нужно.

# Решение:
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
M = []
for x in alphabet[:8]:
    for y in alphabet[:8]:
        A = int(f'{x}01{y}4', 9)
        B = int(f'{x}{y}544', 8)
        if (A + B) % 89 == 0:
            M.append((A + B) // 89)
print(min(M))
'''


# Задание №4:
# В системе счисления с основанием p выполняется равенство 24x9_p + yxy3_p = x4y0_p.
# Буквами x и y обозначены некоторые цифры из алфавита системы счисления с основанием p.
# Определите значение числа xyy_p и запишите это значение в десятичной системе счисления.

# Решение:
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for p in range(10, 36 + 1):
    for x in alphabet[:p]:
        for y in alphabet[:p]:
            if int(f'24{x}9', p) + int(f'{y}{x}{y}3', p) == int(f'{x}4{y}0', p):
                print(int(x + y + y, p))
'''


# 📚 Полезные ссылки на статьи и разборы задач:
# 📘 Полная версия шпаргалки доступна в нашем тг канале: https://t.me/informatika_kege_itpy/362?comment=1424
# 📘 Разборы 14 номеров по информатике: https://t.me/informatika_kege_itpy/360?comment=1535
# 💡Условные операторы if, else, elif а также логические операторы and и or: https://t.me/informatika_kege_itpy/294
# 💡Срезы, что это такое и где могут пригодиться на ЕГЭ: https://t.me/informatika_kege_itpy/351
# endregion (не удаляйте меня, я тут не просто так)


# todo: сюда можно писать заметки, чтобы не забыть задать вопрос репетитору ☝️
progress_result = ()  # Сюда заносятся номера, прорешанных задач.
print('Рекомендуемое кол-во решенных задач для закрепления номера 50.')
print(f'Проверим прогресс: ~{int(len(progress_result) * (100 / 50))}% задач прорешано.')
