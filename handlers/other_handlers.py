from aiogram import Router
from aiogram.types import Message
from lexicon.lexicon_eng import LEXICON_ENG

router: Router = Router()


# Handler for messages that didn't get into other handlers
@router.message()
async def send_answer(message: Message):
    await message.answer(text=LEXICON_ENG['invalid_message_type'])
