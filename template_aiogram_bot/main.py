# region import-ы
from aiogram import Bot, Dispatcher, executor, types

from inline_handlers import *
from keyboard_handlers import *
from library_with_texts import *

import os
import random
import time

with open('token.txt', 'r') as file:
    token = file.readline().strip()

# Вместо token.txt лучше изучать такой способ хранения чувствительной информации
'''  
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('TOKEN_API')
'''

bot = Bot(token)
dp = Dispatcher(bot)


async def on_startup(_):
    print('Я был запущен!')
# endregion import-ы

number = {}


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    number[message.chat.id] = 0
    await message.answer(ForUsers(message).get_text_start(),
                         reply_markup=kb_for_start)


@dp.message_handler(commands=["calculator_game"])
async def command_calculator_game(message: types.Message):
    number[message.chat.id] = 0
    await message.answer(f'The current number is: {number[message.chat.id]}',
                         reply_markup=get_inline_keyboard())


@dp.message_handler()
async def message_handlers(message: types.Message):
    message.text = message.text.lower().strip()
    if message.text == 'привет, друг':
        await message.answer(text=ForUsers(message).welcome_random())
    elif message.text == 'запустим игру?':
        await bot.send_message(chat_id=message.chat.id,
                               text=ForUsers(message).lets_start_game())
    else:
        await message.answer(text=ForUsers(message).echo_answer())


@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith('btn'))
async def handlers_for_callbacks(call: types.CallbackQuery):
    global number
    if call.data == "btn_increase":
        number[call.message.chat.id] += 1
        await call.message.edit_text(ForUsers(call.message).calculate_text() + str(number[call.message.chat.id]),
                                     reply_markup=get_inline_keyboard())
    elif call.data == "btn_decrease":
        number[call.message.chat.id] -= 1
        await call.message.edit_text(ForUsers(call.message).calculate_text() + str(number[call.message.chat.id]),
                                     reply_markup=get_inline_keyboard())
    elif call.data == 'btn_random':
        number[call.message.chat.id] = random.randint(-1000, 1000)
        await call.message.edit_text(ForUsers(call.message).calculate_text() + str(number[call.message.chat.id]),
                                     reply_markup=get_inline_keyboard())


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp,
                           on_startup=on_startup,
                           skip_updates=True)
