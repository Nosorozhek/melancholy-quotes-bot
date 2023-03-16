from aiogram import Router
from aiogram.types import Message
from lexicon.lexicon_eng import LEXICON_ENG

router: Router = Router()


# Хэндлер для сообщений, которые не попали в другие хэндлеры
@router.message()
async def send_answer(message: Message):
    await message.answer(text=LEXICON_ENG['other_answer'])