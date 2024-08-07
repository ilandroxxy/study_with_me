# region 📚 Шпаргалка ЕГЭ | Задание №1

# Задание №1: https://inf-ege.sdamgia.ru/problem?id=58468
# На рисунке схема дорог изображена в виде графа,
# в таблице звёздочками обозначено наличие дороги между населёнными пунктами.
# Так как таблицу и схему рисовали независимо друг от друга, нумерация населённых
# пунктов в таблице никак не связана с буквенными обозначениями на графе.

# Выпишите последовательно без пробелов и знаков препинания указанные на графе буквенные
# обозначения пунктов от П1 до П8: сначала букву, соответствующую П1, затем букву,
# соответствующую П2, и т.д.

# Чистое решение кодом:
'''
from itertools import permutations

table = '14 17 18 23 25 26 32 34 38 41 43 47 48 52 56 58 62 65 71 74 81 83 84 85'
graph = 'АБ БА АИ ИА ИБ БИ ИЖ ЖИ БЖ ЖБ БВ ВБ ВЖ ЖВ ВГ ГВ ЖЕ ЕЖ ЕГ ГЕ ДГ ГД ЕД ДЕ'

for per in permutations('АБВГДЖИЕ'):
    new_table = table
    for i in range(1, 8+1):
        new_table = new_table.replace(str(i), per[i-1])
    if set(new_table.split()) == set(graph.split()):
        print('1 2 3 4 5 6 7 8')
        print(*per)
'''


# 📚 Полезные ссылки на статьи и разборы задач:
# 📘 Полная версия шпаргалки доступна в нашем тг канале: https://t.me/informatika_kege_itpy/362?comment=1424
# 📘 Разборы 1 номеров по информатике: https://t.me/informatika_kege_itpy/360?comment=1460
# endregion (не удаляйте меня, я тут не просто так)


# todo: сюда можно писать заметки, чтобы не забыть задать вопрос репетитору ☝️
progress_result = ()  # Сюда заносятся номера, прорешанных задач.
print('Рекомендуемое кол-во решенных задач для закрепления номера 30.')
print(f'Проверим прогресс: ~{int(len(progress_result) * (100 / 30))}% задач прорешано.')