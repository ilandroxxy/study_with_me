# region Основные команды, используемые в данном задании:
'''
split('A') # разделяет строку по букве A
s = s.replace('SG', '*')  # заменяет все 'SG' на '*'
f = open('24.txt').readlines()  # считывает все строки в файле
'''
# endregion

# region Пример № 1.

# Текстовый файл содержит строки различной длины. Общий объём файла не превышает 1 Мбайт. Строки содержат только заглавные буквы латинского алфавита (ABC…Z).
# В строках, содержащих менее 25 букв A, нужно определить и вывести максимальное расстояние между одинаковыми буквами в одной строке.

# Решение:
'''
f = open('24.txt').readlines()
M = []
for s in f:
    if s.count('A') < 25: # если кол-во букв А меньше 25
        M.append(s)

alphabet = 'QWERTYUIOPASDFGHJKLZXCVBNM'
maxi = 0
for s in M:
    for f in alphabet:
        maxi = max(maxi, s.rindex(f) - s.index(f))
print(maxi)
'''
# endregion

# region Пример № 2.

# Текстовый файл состоит не более чем из 10**6 символов арабских цифр (0,1,...,9).
# Определите максимальное количество идущих подряд цифр, среди которых сумма двух идущих подряд чисел больше числа следующего за ними.
# Для выполнения этого задания следует написать программу.

# Решение:

'''
f = open('24.txt').readline()

count = 1
maxi = 0
for i in range(1, len(f)): # пробегаем по файлу
    if int(f[i-2]) + int(f[i-1]) > int(f[i]): # если сумма двух идущих подряд 
        count += 1                            # чисел больше числа следующего за ними
    else:
        maxi = max(count, maxi)
        count = 1
print(maxi)
'''
# endregion

# region Пример № 3.

# Текстовый файл состоит из символов A, C, D, F и O.
# Определите максимальное количество идущих подряд пар символов вида "согласная + гласная"

# Решение:
'''
f = open('24.txt')
s = f.readline().replace('C', 'S').replace('D', 'S').replace('F', 'S') # заменяем согласные буквы на S
s = s.replace('A', 'G').replace('O', 'G') # заменяем гласные буквы на G
s = s.replace('SG', '*') # Заменяем пару "согласная + гласная" на *
count = 0
maxi = 0
for i in s:
    if i == '*':
        count += 1
        maxi = max(count, maxi)
    else:
        count = 0
print(maxi)
'''
# endregion

# region Пример № 4.

# Текстовый файл состоит не более чем из 1 200 000 символов X, Y, и Z.
# Определите максимальное количество идущих подряд символов, среди которых нет подстроки XZZY.
# Для выполнения этого задания следует написать программу. Ниже приведён файл, который необходимо обработать с помощью данного алгоритма.

# Решение:
'''
f = open('24.txt')
s = f.readline()
M = [len(i) for i in s.split('XZZY')] # разделяем строку по подстроке XZZY
print(max(M)+6)
'''
# endregion