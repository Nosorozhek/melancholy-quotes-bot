import asyncio

from aiogram.filters import BaseFilter
from aiogram.types import Message, InlineQuery


# Custom filter that checks if the message can be converted into a quote
class IsCorrectMessage(BaseFilter):
    def __init__(self, available_letters: set[str] | None) -> None:
        if available_letters is None:
            self.available_letters = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                                      'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6',
                                      '7', '8', '9', '0', '?', '!', ' ', '\n'}
        else:
            self.available_letters = available_letters

    async def __call__(self, message: Message) -> bool:
        for letter in message.text.lower():
            if not (letter in self.available_letters):
                return False
        return True


# Custom filter that checks if the query can be converted into a quote
class IsCorrectInlineQuery(BaseFilter):
    def __init__(self, available_letters: set[str] | None) -> None:
        if available_letters is None:
            self.available_letters = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                                      'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6',
                                      '7', '8', '9', '0', '?', '!', ' ', '\n'}
        else:
            self.available_letters = available_letters

    async def __call__(self, query: InlineQuery) -> bool:
        for letter in query.query.lower()[:-1]:
            if not (letter in self.available_letters):
                return False
        if len(query.query) > 0 and query.query[-1] == '/':
            return True
        return False
