from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.methods import SendPhoto, AnswerCallbackQuery
from aiogram.types import Message, BufferedInputFile, FSInputFile, InlineQueryResultCachedPhoto
from aiogram.handlers import InlineQueryHandler

from PIL import Image
from time import time
import datetime

from lexicon.lexicon_eng import LEXICON_ENG
from filters.filters import IsCorrectMessage, IsCorrectInlineQuery
from services.text_processing import Quote
from services.image_processing import create_quote_image
from config_data.config import Config, load_config

router: Router = Router()

config: Config = load_config()


# This handler is triggered by the command /start
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_ENG['/start'])
    print(message.chat.id)


# This handler is triggered by the command /help
@router.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_ENG['/help'])


# TODO: make it a class field
available_letters: set[str] = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                               's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
                               '?', '!', ' ', '\n'}


# This handler is triggered if the text can be converted into a quote
@router.message(IsCorrectMessage(available_letters))
async def process_help_command(message: Message):
    try:
        t: float = time()
        logs = open("logs.txt", "a")
        quote = Quote(message.text)
        quote_image: Image = create_quote_image(quote, None).resize((800, 533))
        quote_image.save("cash/" + quote.filename + ".png", "PNG")
        img: FSInputFile = FSInputFile("cash/" + quote.filename + ".png", quote.quote[0] + ".png")
        dt = datetime.datetime.now()
        server_time = dt.strftime("%H:%M %m/%d/%Y\n")
        logs.write(server_time)
        if message.chat.last_name is not None:
            logs.write(message.chat.first_name + " " + message.chat.last_name + ":\n«" + quote.text + "»\n")
        else:
            logs.write(message.chat.first_name + ":\n«" + quote.text + "»\n")
        print(time() - t)
        await message.answer_photo(img)
    except:
        await message.answer(text=LEXICON_ENG['exception'])


# Inline mode
@router.inline_query(IsCorrectInlineQuery(available_letters))
async def handler(query: InlineQueryHandler):
    quote = Quote(query.query)
    quote_image: Image = create_quote_image(quote, None).resize((800, 533))
    quote_image.save("cash/" + quote.filename + ".png", "PNG")
    img: FSInputFile = FSInputFile("cash/" + quote.filename + ".png", quote.filename + ".png")
    id_photo = await SendPhoto(chat_id=config.tg_bot.bot_channel_id,
                               photo=img)
    await AnswerCallbackQuery(callback_query_id=InlineQueryResultCachedPhoto(type='photo', id=query.from_user.id,
                                                                             photo_file_id=id_photo.photo[
                                                                                 0].file_id).photo_file_id)
