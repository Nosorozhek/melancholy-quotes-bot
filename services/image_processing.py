import random

from PIL import Image

from services.text_processing import Quote


def create_quote_image(quote: Quote, bg_path: str | None) -> Image:
    if bg_path is None:
        bg_path = r"art/background.png"
    quote_image: Image = Image.open(bg_path)  # .resize((4800 * 2, 3200 * 2))
    height: float = (len(quote.quote) * 1.5 - 0.5) * quote.alphabet.max_height
    y: float = (quote_image.height - height) / 2 + quote.alphabet.max_height * 0.5
    for line in quote.quote:
        width: int = 0
        letters: list[Image] = []
        for i in line:
            if i == ' ':
                letters.append(None)
                width += quote.alphabet.avg_width
            elif i != '\n':
                letters.append(quote.alphabet.letters[i][random.randint(0, len(quote.alphabet.letters[i]) - 1)])
                width += letters[len(letters) - 1].width
        x: int = int((quote_image.width - width) / 2)
        for i in letters:
            if i is None:
                x += quote.alphabet.avg_width
            else:
                left: int = int(x + i.width * 0.05)
                top: int = int(y - i.height * 0.45)
                x += i.width
                i = i.resize((int(i.width * 0.9), int(i.height * 0.9)))
                quote_image.paste(i, (left, top, left + i.width, top + i.height), i)
        y += quote.alphabet.max_height * 1.5
    # quote_image.resize((800, 533))
    return quote_image
