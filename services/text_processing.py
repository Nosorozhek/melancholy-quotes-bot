from random import randint
from PIL import Image
from image_processing import ANONYMOUS_ALPHABET

MAX_LENGTH: int = 5000


class Letter:
    def __init__(self, letter: str, img: Image = None):
        if img is None:
            img = ANONYMOUS_ALPHABET[letter][0]
        self.img = img
        self.letter = letter
        self.width: int = img.width


class Quote:
    def __init__(self, text: str, alphabet: dict[str, Image] = None):
        if alphabet is None:
            alphabet = ANONYMOUS_ALPHABET
        self.alphabet = alphabet
        self.text = text
        self.lines: list[str]

    def split_into_lines(self, text: str) -> list[list[str | int]]:
        quote: list[list[str | int]] = []
        length: list[int] = []
        for letter in text:
            quote.append([letter, randint(0, len(ANONYMOUS_ALPHABET[letter]) - 1)])
            list.append(ANONYMOUS_ALPHABET[letter][quote[len(quote) - 1][1]])
        return quote

    def _get_part_text(self, text: str, start: int, page_size: int) -> tuple[str, int]:
        last_end: int = start
        curr: int = start
        while curr < min(page_size + start - 1, len(text) - 1):
            curr += 1
            if text[curr] == ' ':
                last_end = curr
        return text[start:last_end + 1], last_end - start + 1
