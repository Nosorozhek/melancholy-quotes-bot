from random import randint
from PIL import Image
from services.alphabet_generator import Alphabet, ANONYMOUS_ALPHABET

MAX_LENGTH: int = 5000


class Quote:
    def __init__(self, text: str, alphabet: Alphabet = None):
        if alphabet is None:
            alphabet = ANONYMOUS_ALPHABET
        self.alphabet = alphabet
        self.text = text.lower() + ' '
        self.quote: list[str] = []
        self.line_size: int = 533
        self.split_into_lines(self.text)
        # self.print()

    def get_part_of_text(self, start: int, page_size: int) -> tuple[str, int]:
        last_end: int = start
        curr: int = start
        length: int = 0
        while length < page_size and curr < len(self.text) - 1:
            curr += 1
            length += self.alphabet.avg_width
            if self.text[curr] == ' ':
                last_end = curr
            if self.text[curr] == '\n':
                last_end = curr - 1
                break
        if last_end == start:
            last_end = curr
        return self.text[start:last_end + 1], last_end - start + 1

    def split_into_lines(self, text: str):
        self.quote = []
        curr: int = 0
        while curr < len(text):
            line: str
            length: int
            line, length = self.get_part_of_text(curr, self.line_size)
            while line[len(line) - 1] == ' ':
                line = line[:len(line) - 1]
            self.quote.append(line)
            curr += length

    def print(self):
        print("---")
        for line in self.quote:
            print("   ", line)
        print("---")
