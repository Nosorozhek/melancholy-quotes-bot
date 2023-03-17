from PIL import Image

ANONYMOUS_ALPHABET: dict[str, Image]


def _generate_alphabet():
    alphabet_image = Image.open(r"../art/anonymous font transparent.png")
    alphabet_image.show()
    width, height = alphabet_image.size
    print(width, height)

    metafile = open("../art/metafile.txt", "r")
    s: str = metafile.read()

    letter_x: list[int] = []
    letter_y: list[int] = []
    letter_width: list[int] = []
    letter_height: list[int] = []

    for i in range(len(s)):
        if s[i - 3:i + 1] == " x: ":
            letter_x.append(int(s[i + 1] + s[i + 2] + s[i + 3] + s[i + 4]))
        if s[i - 4:i + 1] == "  y: ":
            letter_y.append(height - int(s[i + 1] + s[i + 2] + s[i + 3] + s[i + 4]))
        if s[i - 6:i + 1] == "width: ":
            letter_width.append(int(s[i + 1] + s[i + 2] + s[i + 3] + s[i + 4]))
        if s[i - 7:i + 1] == "height: ":
            letter_height.append(int(s[i + 1] + s[i + 2] + s[i + 3] + s[i + 4]))

    letter_images: list[Image] = []

    for i in range(len(letter_x)):
        if letter_width[i] < 10 or letter_height[i] < 10:
            pass
        left: int = letter_x[i]
        top: int = letter_y[i] - letter_height[i]
        right: int = left + letter_width[i]
        bottom: int = top + letter_height[i]
        # print(left, top, right, bottom)
        letter_images.append(alphabet_image.crop((left, top, right, bottom)))

    letters: list[str] = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                          't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
                          'question mark', 'exclamation mark']

    global ANONYMOUS_ALPHABET
    ANONYMOUS_ALPHABET: dict[str, Image] = {}
    for i in range(len(letter_images)):
        letter_images[i].save(r"art\anonymous font\letter_{}_{}.png".format(letters[int(i / 6)], i % 6))
        print(r"art\anonymous font\letter_{}_{}.png".format(letters[int(i / 6)], i % 6))
        if letters[int(i / 6)] == 'question mark':
            ANONYMOUS_ALPHABET['?'].append(letter_images[i])
        if letters[int(i / 6)] == 'exclamation mark':
            ANONYMOUS_ALPHABET['!'].append(letter_images[i])
        else:
            ANONYMOUS_ALPHABET[letters[int(i / 6)]].append(letter_images[i])


_generate_alphabet()
