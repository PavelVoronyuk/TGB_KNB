from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command, CommandStart

from lexicon.lexicon_ru import LEXICON_RU
from keyboards.keyboards import keyboard_game, keyboard_start
from funcs.funcs import rps, winner

router = Router()

@router.message(CommandStart())
async def start(message: Message):
    await message.answer(text=LEXICON_RU["/start"],
                         reply_markup=keyboard_start)

@router.message(Command(commands="help"))
async def comm_help(message: Message):
    await message.answer(text=LEXICON_RU["/help"],
                         reply_markup=keyboard_start)

@router.message(F.text == LEXICON_RU["yes"])
async def starting_game(message: Message):
    await message.answer(text=LEXICON_RU["yes_answ"],
                         reply_markup=keyboard_game)

@router.message(F.text == LEXICON_RU["no"])
async def starting_game(message: Message):
    await message.answer(text=LEXICON_RU["no_answ"],
                         reply_markup=keyboard_start)

@router.message(F.text.in_([LEXICON_RU["rock"],
                            LEXICON_RU["paper"],
                            LEXICON_RU["scissors"]]))
async def process_game(message: Message):
    the_choice = rps()
    await message.answer(text=f"Бот выбрал {LEXICON_RU[the_choice]}")

    win = winner(message.text ,the_choice)
    await message.answer(text=LEXICON_RU[win], reply_markup=keyboard_start)
