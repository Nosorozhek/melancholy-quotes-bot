from aiogram import Router
from aiogram.filters import Command, CommandStart, BaseFilter
from aiogram.types import Message
from lexicon.lexicon_eng import LEXICON_ENG

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


# Custom filter that checks if the message can be converted into a quote
class CorrectMessage(BaseFilter):
    def __init__(self, available_letters: set[str]) -> None:
        self.available_letters = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
                                  'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8',
                                  '9', '0', '?', '!'}

    async def __call__(self, message: Message) -> bool:
        for letter in message.text:
            if not (letter in self.available_letters):
                return False
        return True

    # This handler is triggered if the text can be converted into a quote
    @router.message(CorrectMessage(available_letters))
    async def process_help_command(message: Message):
        await message.answer(text=LEXICON_ENG['/help'])
