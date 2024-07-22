
# region 📚 Шпаргалка ЕГЭ | Задание №11

# Задание №1:
# При регистрации в компьютерной системе каждому объекту присваивается идентификатор, состоящий из 235 символов и
# содержащий символы из 30-символьного набора букв.
# В базе данных для хранения каждого идентификатора отведено одинаковое и минимально возможное целое число бит.
# При этом используется посимвольное кодирование идентификаторов,
# все символы кодируются одинаковым и минимально возможным количеством бит.
# Определите объём памяти (в Мбайт), необходимый для хранения 71 698 идентификаторов.
# В ответе запишите только целую часть числа.

# Решение:
'''
symbols = 235
alphabet = 30
i = 5
bit = symbols * i
mbyte = (bit * 71698) / 2 ** 23
print(mbyte)
'''


# Задание №2:
# При регистрации в компьютерной системе каждому пользователю выдаётся пароль, состоящий из 35 символов
# и содержащий только десятичные цифры и символы из 4090-символьного специального алфавита.
# В базе данных для хранения сведений о каждом пользователе отведено одинаковое и минимально возможное целое число байт.
# При этом используют посимвольное кодирование паролей, все символы кодируют одинаковым и минимально возможным
# количеством бит.
# Кроме собственно пароля, для каждого пользователя в системе хранятся дополнительные сведения,
# для чего выделено целое число байт; это число одно и то же для всех пользователей.
# Для хранения сведений о 300 пользователях потребовалось 96000 байт.
# Сколько байт выделено для хранения дополнительных сведений об одном пользователе?
# В ответе запишите только целое число – количество байт.

# Решение:
'''
symbols = 35
alphabet = 4090 + 10
i = 13
bit = symbols * i
byte = int(bit / 8) + 1
all_info = 96000 / 300
dop_info = all_info - byte
print(dop_info)
'''


# 📚 Полезные ссылки на статьи и разборы задач:
# 📘 Полная версия шпаргалки доступна в нашем тг канале: https://t.me/informatika_kege_itpy/362?comment=1424
# 📘 Разборы 11 номеров по информатике: https://t.me/informatika_kege_itpy/360?comment=1496
# 💡 Учимся работать с единицами измерения информации: https://t.me/informatika_kege_itpy/386
# endregion (не удаляйте меня, я тут не просто так)


# todo: сюда можно писать заметки, чтобы не забыть задать вопрос репетитору ☝️
progress_result = ()  # Сюда заносятся номера, прорешанных задач.
print('Рекомендуемое кол-во решенных задач для закрепления номера 30.')
print(f'Проверим прогресс: ~{int(len(progress_result) * (100 / 30))}% задач прорешано.')
