from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from lexicon.lexicon_ru import LEXICON_RU

btn_rock = KeyboardButton(text=LEXICON_RU["rock"])
btn_paper = KeyboardButton(text=LEXICON_RU["paper"])
btn_scissors = KeyboardButton(text=LEXICON_RU["scissors"])

keyboard_game = ReplyKeyboardMarkup(keyboard=[[btn_rock],
                                              [btn_paper],
                                              [btn_scissors]],
                                       resize_keyboard=True)

btn_yes = KeyboardButton(text=LEXICON_RU["yes"])
btn_no = KeyboardButton(text=LEXICON_RU["no"])

keyboard_start = ReplyKeyboardMarkup(keyboard=[[btn_yes],[btn_no]])