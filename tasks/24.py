
# region 📚 Шпаргалка ЕГЭ | Задание №24

# Задание №1:
# Текстовый файл состоит из заглавных букв латинского алфавита Q, R, W и цифр 1, 2, 4.
# Определите в прилагаемом файле максимальное количество идущих подряд символов,
# среди которых ни одна буква не стоит рядом с буквой, а цифра – с цифрой.

# Решение:
'''
s = open('24.txt').readline()
s = s.replace('1', '2').replace('4', '2')
s = s.replace('Q', 'R').replace('W', 'R')
while '22' in s or 'RR' in s:
    s = s.replace('RR', 'R R').replace('22', '2 2')
print(max([len(x) for x in s.split()]))
'''


# Задание №2:
# Текстовый файл состоит из символов K, L, M и N.
# В прилагаемом файле определите максимальное количество символов в непрерывной подпоследовательности,
# состоящей из идущих подряд групп символов KLMN в указанном порядке, при этом в начале
# и в конце искомой последовательности группа символов KLMN может быть неполной.

# Решение:
'''
s = open('24.txt').readline()
count = 3
maxi = 0
for i in range(len(s)-3):
    if s[i:i+4] in ('KLMN', 'LMNK', 'MNKL', 'NKLM'):
        count += 1
        maxi = max(maxi, count)
    else:
        count = 3
print(maxi)
'''


# Задание №3:
# Текстовый файл состоит из символов, обозначающих заглавные буквы
# латинского алфавита и цифры от 1 до 9 включительно.
# Определите в прилагаемом файле максимальное количество идущих подряд символов,
# которые могут представлять запись числа в шестнадцатеричной системе счисления.

# Решение:
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
s = open('24.txt').readline()
for x in alphabet[16:]:
    s = s.replace(x, ' ')
print(max([len(x) for x in s.split() if x[0] != '0']))
'''


# Задание №4:
# Текстовый файл состоит из символов, обозначающих прописные буквы латинского алфавита.
# Определите максимальное количество идущих подряд символов, среди которых никакие
# две буквы из набора букв N, O и P (с учетом повторений) не записаны подряд.

# Решение:
'''
s = open('24.txt').readline()
s = s.replace('N', 'O').replace('O', 'P')
while 'PP' in s:
    s = s.replace('PP', 'P P')
print(max(len(x) for x in s.split()))
'''


# Задание №5:
# Текстовый файл состоит из символов A, C, D, F и U.
# Определите максимальное количество идущих подряд пар символов вида согласная + гласная в прилагаемом файле.

# Решение:
'''
s = open('24.txt').readline()
s = s.replace('U', 'A').replace('C', 'F').replace('F', 'D')
s = s.replace('DA', '*')
s = s.replace('D', ' ').replace('A', ' ')
print(max([len(x) for x in s.split()]))
'''


# Задание №6:
# Текстовый файл состоит из символов С, D, Е и F.
# Определите максимальное количество идущих подряд последовательностей символов CFE или FCE в прилагаемом файле.
# Искомая подпоследовательность должна состоять только из троек CFE, или только из троек FCE,
# или только из троек CFE или FCE в произвольном порядке их следования.

# Решение:
'''
s = open('24.txt').readline()
s = s.replace('CFE', '*').replace('FCE', '*')
for x in 'CDEF':
    s = s.replace(x, ' ')
print(max([len(x) for x in s.split()]))
'''


# Задание №7:
# Текстовый файл состоит из символов T, U, V, W, X, Y и Z.
# Определите в прилагаемом файле максимальное количество идущих подряд символов
# (длину непрерывной подпоследовательности), среди которых символ T встречается ровно 100 раз.

# Решение:
'''
s = open('24.txt').readline().split('T')
maxi = 0
for i in range(len(s)-100):
    r = 'T'.join(s[i:i+101])
    maxi = max(maxi, len(r))
print(maxi)
'''


# Задание №8:
# Текстовый файл состоит из символов T, U, V, W, X, Y и Z.
# Определите в прилагаемом файле минимальное количество идущих подряд символов
# (длину непрерывной подпоследовательности), среди которых символ X встречается не менее 500 раз,
# а символ Y не встречается совсем.

# Решение:
'''
s = open('24.txt').readline().split('X')
mini = 10**9
for i in range(len(s)-498):
    r = 'X' + 'X'.join(s[i:i+499]) + 'X'
    if 'Y' not in r:
        mini = min(mini, len(r))
print(mini)
'''


# 📚 Полезные ссылки на статьи и разборы задач:
# 📘 Полная версия шпаргалки доступна в нашем тг канале: https://t.me/informatika_kege_itpy/362?comment=1424
# 📘 Разборы 24 номеров по информатике: https://t.me/informatika_kege_itpy/360?comment=2706
# endregion (не удаляйте меня, я тут не просто так)


# todo: сюда можно писать заметки, чтобы не забыть задать вопрос репетитору ☝️
progress_result = ()  # Сюда заносятся номера, прорешанных задач.
print('Рекомендуемое кол-во решенных задач для закрепления номера 80.')
print(f'Проверим прогресс: ~{int(len(progress_result) * (100 / 80))}% задач прорешано.')