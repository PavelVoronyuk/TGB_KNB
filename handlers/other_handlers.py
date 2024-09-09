from lexicon.lexicon_ru import LEXICON_RU

from aiogram import Router
from aiogram.types import Message

router = Router()

@router.message()
async def other_messages(message: Message):
    await message.reply(text=LEXICON_RU["other"])