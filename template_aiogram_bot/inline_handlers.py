from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
# emojis = "😅🙏😂😭😄😢😍❤️😁👍👎☺️😱😌🥳😎👾🤖💙💚💫💥💣💯💭👈👉👇"


def get_inline_keyboard() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [
             InlineKeyboardButton('Increase', callback_data='btn_increase'),
             InlineKeyboardButton('Decrease', callback_data='btn_decrease')
        ],
        [
            InlineKeyboardButton('Random number', callback_data='btn_random')
        ]
    ])
    return ikb
