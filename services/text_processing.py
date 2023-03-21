from random import randint
from PIL import Image
from image_processing import ANONYMOUS_ALPHABET

MAX_LENGTH: int = 5000


class Quote:
    def __init__(self, text: str, alphabet: dict[str, Image] = None):
        if alphabet is None:
            alphabet = ANONYMOUS_ALPHABET
        self.alphabet = alphabet
        self.text = text
        self.quote: list[str] = []
        self.line_size: int = 20
        self.split_into_lines(self.text)
        self.print()

    def get_part_of_text(self, start: int, page_size: int) -> tuple[str, int]:
        last_end: int = start
        curr: int = start
        length: int = 0
        while curr < min(page_size + start - 1, len(self.text) - 1):
            curr += 1
            length += self.alphabet.avg_width
            if self.text[curr] == ' ':
                last_end = curr
        return self.text[start:last_end + 1], last_end - start + 1

    def split_into_lines(self, text: str):
        self.quote = []
        curr: int = 0
        while curr < len(text):
            line: str
            length: int
            line, length = self.get_part_of_text(curr, self.line_size)
            self.quote.append(line)
            curr += length

    def print(self):
        print("---")
        for line in self.quote:
            print("   ", line)
        print("---")