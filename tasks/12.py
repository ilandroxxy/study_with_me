# region Основные команды, используемые в данном задании:
'''
s = s.replace('1', '2', 1)  # заменяет 1 на 2 в строке один раз
for n in range(4, 100):  # перебор количества цифр
s = '2' + '5' * n    # составляем строку из условия
while '25' in s   # пока 25 не будет найдено в строке
s.count('3')  # кол-во цифр 3 в строке
'''
# endregion

# region Пример № 1.

# Дана программа для редактора:

# НАЧАЛО
# ПОКА нашлось (25) ИЛИ нашлось (355) ИЛИ нашлось (555)
#   ЕСЛИ нашлось (25)
#     ТО заменить (25, 5)
#   КОНЕЦ ЕСЛИ
#   ЕСЛИ нашлось (355)
#     ТО заменить (355, 52)
#   КОНЕЦ ЕСЛИ
#   ЕСЛИ нашлось (555)
#     ТО заменить (555, 3)
#   КОНЕЦ ЕСЛИ
# КОНЕЦ ПОКА
# КОНЕЦ

# На вход приведённой выше программе поступает строка, начинающаяся с цифры "2", а затем содержащая n цифр "5" (n > 3).
# Определите наименьшее значение n, при котором в строке, получившейся в результате выполнения программы, количество цифр «3» равно 2.

# Решение:

'''
for n in range(4, 100):    # перебираем количество цифр 5
    s = '2' + '5' * n      # составляем строку из условия
    while '25' in s or '355' in s or '555' in s:
        if '25' in s:
            s = s.replace('25', '5', 1)
        if '355' in s:
            s = s.replace('355', '52', 1)
        if '555' in s:
            s = s.replace('555', '3', 1)
    if s.count('3') == 2:  # если в полученной строке количество цифр «3» равно 2
        print(n)
        break
'''
# endregion