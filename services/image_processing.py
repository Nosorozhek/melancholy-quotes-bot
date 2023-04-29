from random import randint
from PIL import Image
from services.text_processing import Quote


def create_quote_image(quote: Quote, bg_path: str | None) -> Image:
    if bg_path is None:
        bg_path = r"art/background.png"
    quote_image: Image = Image.open(bg_path)
    height: float = ((len(quote.quote) - 1) * quote.font.line_height + 1) * quote.font.max_height
    y: float = (quote_image.height - height) / 2 + quote.font.max_height / 2
    for line in quote.quote:
        width: int = 0
        letters: list[Image] = []
        for i in line:
            if i == ' ':
                letters.append(None)
                width += quote.font.avg_width
            elif i != '\n':
                letters.append(quote.font.letters[i][randint(0, len(quote.font.letters[i]) - 1)])
                width += letters[len(letters) - 1].width
        x: int = int((quote_image.width - width) / 2)
        for i in letters:
            if i is None:
                x += quote.font.avg_width
            else:
                left: int = int(x + i.width * quote.font.letter_spacing / 2)
                top: int = int(y - i.height * (1 - quote.font.letter_spacing) / 2)
                x += i.width
                i = i.resize(
                    (int(i.width * (1 - quote.font.letter_spacing)), int(i.height * (1 - quote.font.letter_spacing))))
                quote_image.paste(i, (left, top, left + i.width, top + i.height), i)
                quote_image.paste(i, (left, top, left + i.width, top + i.height), i)
        y += quote.font.max_height * quote.font.line_height
    return quote_image
