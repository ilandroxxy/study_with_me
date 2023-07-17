from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

kb_for_start = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
kb_btn1 = KeyboardButton('Привет, друг')
kb_btn2 = KeyboardButton('Запустим игру?')
kb_for_start.add(kb_btn1, kb_btn2)
