from aiogram.filters import BaseFilter
from aiogram.types import Message


# Custom filter that checks if the message can be converted into a quote
class IsCorrectMessage(BaseFilter):
    def __init__(self, available_letters: set[str]) -> None:
        self.available_letters = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
                                  'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8',
                                  '9', '0', '?', '!', ' ', '\n'}

    async def __call__(self, message: Message) -> bool:
        for letter in message.text:
            if not (letter in self.available_letters):
                return False
        return True
