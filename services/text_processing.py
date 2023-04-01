from random import randint
from PIL import Image
from services.fonts import Font, ANONYMOUS_FONT

MAX_LENGTH: int = 5000


class Quote:
    def __init__(self, text: str = ' ', font: Font = None):
        if font is None:
            font = ANONYMOUS_FONT
        self.font = font
        self.text = text.lower().rstrip()
        self.quote: list[str] = []
        self.line_size: int = 650
        self.split_into_lines(self.text)
        self.filename = self.quote[0].replace('?', '').replace('!', ' ')
        # self.print()

    # A method that returns the maximum length of a string that will fit into the picture
    def get_part_of_text(self, start: int, line_size: int) -> tuple[str, int]:
        last_end: int = start
        curr: int = start + 1
        length: int = 0
        while length < line_size and curr < len(self.text):
            length += self.font.avg_width
            if self.text[curr] == ' ':
                last_end = curr
            if self.text[curr] == '\n':
                last_end = curr - 1
                break
            curr += 1
        if last_end == start or length < line_size:
            last_end = curr
        return self.text[start:last_end + 1], last_end - start + 1

    # A method that splits the quote text into the lines
    def split_into_lines(self, text: str):
        self.quote = []
        curr: int = 0
        while curr < len(text):
            line: str
            length: int
            line, length = self.get_part_of_text(curr, self.line_size)
            while line[len(line) - 1] == ' ' or line[len(line) - 1] == '\n':
                line = line[:len(line) - 1]
            self.quote.append(line)
            curr += length

    # Method that just outputs the quote in the console
    def print(self):
        print("---")
        for line in self.quote:
            print("   ", line)
        print("---")
