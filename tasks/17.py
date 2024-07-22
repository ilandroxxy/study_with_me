
# region 📚 Шпаргалка ЕГЭ | Задание №17

# Задание №1:
# В файле содержится последовательность натуральных чисел.
# Элементы последовательности могут принимать целые значения от 1 до 100 000 включительно.
# Определите количество пар последовательности, в которых хотя бы одно число делится на
# минимальный элемент последовательности, кратный 21.
# Гарантируется, что такой элемент в последовательности есть.
# В ответе запишите количество найденных пар, затем максимальную из сумм элементов таких пар.
# В данной задаче под парой подразумевается два идущих подряд элемента последовательности.

# Решение:
'''
M = [int(i) for i in open('17.txt')]
D = [int(i) for i in M if i % 21 == 0]
R = []
for i in range(len(M) - 1):
    x, y = M[i:i+2]
    if (x % min(D) == 0) or (y % min(D) == 0):
        R.append(x + y)
print(len(R), max(R))
'''


# Задание №2:
# В файле содержится последовательность целых чисел.
# Элементы последовательности могут принимать целые значения от —100 000 до 100 000 включительно.
# Определите количество троек элементов последовательности, в которых хотя бы один из трёх элементов оканчивается на 3,
# а сумма элементов тройки не больше максимального элемента последовательности, являющегося пятизначным числом,
# которое оканчивается на 3.
# В ответе запишите количество найденных троек чисел,
# затем максимальную из сумм элементов таких троек.
# В данной задаче под тройкой подразумевается три идущих подряд элемента последовательности.

# Решение:
'''
M = [int(i) for i in open('17.txt')]
D = [i for i in M if str(i)[-1] == '3']
B = [i for i in D if len(str(i)) == 5]
R = []
for i in range(len(M) - 2):
    x, y, z = M[i:i+3]
    if (x in D) or (y in D) or (z in D):
        R.append(x + y + z)
print(len(R), max(R))
'''


# Задание №3:
# В файле содержится последовательность целых неотрицательных чисел, не превышающих 10000.
# Определите количество пар элементов последовательности, в которых либо сумма элементов кратна 18,
# либо произведение элементов кратно 18.
# В ответе запишите два числа: сначала количество найденных пар, затем максимальную сумму элементов этих пар.
# В данной задаче под парой подразумевается два различных элемента последовательности.

# Решение:
'''
M = [int(i) for i in open('17.txt')]
R = []
for i in range(len(M)):
    for j in range(i + 1, len(M)):
        x, y = M[i], M[j]
        if ((x + y) % 18 == 0) ^ ((x + y) % 18 != 0):
            R.append(x + y)
print(len(R), max(R))
'''


# 📚 Полезные ссылки на статьи и разборы задач:
# 📘 Полная версия шпаргалки доступна в нашем тг канале: https://t.me/informatika_kege_itpy/362?comment=1424
# 📘 Разборы 17 номеров по информатике: https://t.me/informatika_kege_itpy/360?comment=1612
# 💡 Генераторы списков (списочные выражения) для ЕГЭ: https://t.me/informatika_kege_itpy/339
# 💡 Работа с файлами Python: https://t.me/informatika_kege_itpy/286
# 🐍 Примеры работы с .txt файлами на некоторых номерах ЕГЭ: https://t.me/informatika_kege_itpy/400
# 🐍 Шпаргалка по генераторам списков: https://t.me/informatika_kege_itpy/495
# endregion (не удаляйте меня, я тут не просто так)


# todo: сюда можно писать заметки, чтобы не забыть задать вопрос репетитору ☝️
progress_result = ()  # Сюда заносятся номера, прорешанных задач.
print('Рекомендуемое кол-во решенных задач для закрепления номера 50.')
print(f'Проверим прогресс: ~{int(len(progress_result) * (100 / 50))}% задач прорешано.')
