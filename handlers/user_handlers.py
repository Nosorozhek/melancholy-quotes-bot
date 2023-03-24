from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, BufferedInputFile, FSInputFile
from lexicon.lexicon_eng import LEXICON_ENG

from PIL import Image
from time import time

from filters.filters import IsCorrectMessage
from services.text_processing import Quote
from services.image_processing import create_quote_image

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
                               '?', '!', ' ', '\n'}


# This handler is triggered if the text can be converted into a quote
@router.message(IsCorrectMessage(available_letters))
async def process_help_command(message: Message):
    t: float = time()
    logs = open("logs.txt", "a")
    quote = Quote(message.text)
    quote_image: Image = create_quote_image(quote, None).resize((800, 533))
    # quote_image.show()
    quote_image.save("cash/" + quote.quote[0] + ".png", "PNG")
    # img: BufferedInputFile = BufferedInputFile(quote_image.tobytes(), "here comes .png")
    img: FSInputFile = FSInputFile("cash/" + quote.quote[0] + ".png", quote.quote[0] + ".png")
    logs.write("---\n" + quote.text + "\n---\n")
    print(time() - t)
    await message.answer_photo(img)
