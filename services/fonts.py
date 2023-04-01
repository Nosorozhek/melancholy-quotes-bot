from PIL import Image
from dataclasses import dataclass
import json


@dataclass
class Font:
    letters: dict[str, list[Image]]
    avg_width: float
    max_height: float
    line_height: float
    letter_spacing: float


def load_font(name: str = "anonymous font"):
    f = open("art/{}/data.json".format(name))
    data = json.load(f)
    letters: dict[str, list[Image]] = {}
    for letter in data["letters"]:
        letters[letter[0]] = []
        for i in range(letter[1]):
            if letter[0] == "question mark" or letter[0] == "exclamation mark":
                continue
            if letter[0] == '?':
                letters['?'].append(Image.open(r"art/{}/letters/letter_{}_{}.png".format(name, "question mark", i)))
            elif letter[0] == '!':
                letters['!'].append(Image.open(r"art/{}/letters/letter_{}_{}.png".format(name, "exclamation mark", i)))
            else:
                letters[letter[0]].append(Image.open(r"art/{}/letters/letter_{}_{}.png".format(name, letter[0], i)))
    font: Font = Font(letters, data["avg_width"], data["max_height"], data["line_height"], data["letter_spacing"])
    f.close()
    return font


ANONYMOUS_FONT: Font = load_font()
