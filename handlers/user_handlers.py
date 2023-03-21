from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from lexicon.lexicon_eng import LEXICON_ENG

from filters.filters import IsCorrectMessage
from services.text_processing import Quote

router: Router = Router()


# This handler is triggered by the command /start
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_ENG['/start'])


# This handler is triggered by the command /help
@router.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_ENG['/help'])


available_letters: set[str] = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                               's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
                               '?', '!'}


# This handler is triggered if the text can be converted into a quote
@router.message(IsCorrectMessage(available_letters))
async def process_help_command(message: Message):
    quote = Quote(message.text)
    await message.answer('\n'.join(quote.quote))
