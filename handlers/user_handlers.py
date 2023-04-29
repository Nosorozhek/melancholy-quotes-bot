import asyncio

from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.methods import SendPhoto, AnswerInlineQuery
from aiogram.types import Message, FSInputFile, InlineQueryResultCachedPhoto, InlineQuery
from aiogram.exceptions import TelegramRetryAfter

from PIL import Image
from time import time

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
                               '?', '!', '.', ' ', '\n'}


# This handler is triggered if the text can be converted into a quote
@router.message(IsCorrectMessage(available_letters))
async def process_help_command(message: Message):
    try:
        t: float = time()
        quote = Quote(message.text)
        quote_image: Image = create_quote_image(quote, None)
        quote_image.save("cash/" + quote.filename + ".png", "PNG")
        img: FSInputFile = FSInputFile("cash/" + quote.filename + ".png", quote.filename + ".png")
        print(time() - t)
        await message.answer_photo(img)
    except:
        await message.answer(text=LEXICON_ENG['exception'])


# Inline mode handler
@router.inline_query(IsCorrectInlineQuery(available_letters))
async def handler(query: InlineQuery):
    quote = Quote(query.query[:-1])
    quote_image: Image = create_quote_image(quote, None).resize((800, 533))
    quote_image.save("cash/" + quote.filename + ".png", "PNG")
    img: FSInputFile = FSInputFile("cash/" + quote.filename + ".png", quote.filename + ".png")
    try:
        msg = await SendPhoto(chat_id=config.tg_bot.bot_channel_id, photo=img)
    except TelegramRetryAfter as e:
        await asyncio.sleep(e.retry_after)
        msg = await SendPhoto(chat_id=config.tg_bot.bot_channel_id, photo=img)
    results = [InlineQueryResultCachedPhoto(type='photo', id=query.from_user.id, photo_file_id=msg.photo[0].file_id)]
    await AnswerInlineQuery(inline_query_id=query.id, results=results, cache_time=5)
