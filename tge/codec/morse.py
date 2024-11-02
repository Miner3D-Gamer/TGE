def encode(message: str) -> str:
    """
    Encode a given message into Morse code.

    This function takes a string message and encodes it into Morse code
    using a predefined dictionary of characters and their corresponding
    Morse code representations.

    Args:
        message (str): The message to be encoded into Morse code.

    Returns:
        str: The encoded message in Morse code.
    """
    morse_code = {
        "a": ".-",
        "b": "-...",
        "c": "-.-.",
        "d": "-..",
        "e": ".",
        "f": "..-.",
        "g": "--.",
        "h": "....",
        "i": "..",
        "j": ".---",
        "k": "-.-",
        "l": ".-..",
        "m": "--",
        "n": "-.",
        "o": "---",
        "p": ".--.",
        "q": "--.-",
        "r": ".-.",
        "s": "...",
        "t": "-",
        "u": "..-",
        "v": "...-",
        "w": ".--",
        "x": "-..-",
        "y": "-.--",
        "z": "--..",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        "0": "-----",
        ",": "--..--",
        ".": ".-.-.-",
        "?": "..--..",
        "/": "-..-.",
        "-": "-....-",
        "(": "-.--.",
        ")": "-.--.-",
        "&": ".-...",
        "@": ".--.-.",
        "!": "-.-.--",
        "$": "...-..-",
        "%": ".-.-.",
        "=": "-...-",
        "+": ".-.-.",
        "_": "..--.-",
        '"': ".-..-.",
        "<": ".-.-",
        ">": ".-..-.",
        ":": "---...",
        ";": "-.-.-.",
        " ": "/",
    }

    return "".join([morse_code[letter] for letter in message.lower()])


def decode(message: str) -> str:
    """
    Decodes a Morse code message into plain text.

    Args:
        message (str): The Morse code message to be decoded.

    Returns:
        str: The decoded plain text message.

    Morse code dictionary:
        The function uses a predefined dictionary `morse_code` to map Morse code sequences
        to their corresponding plain text characters. Each character is separated by a space.
    """
    morse_code = {
        ".-": "a",
        "-...": "b",
        "-.-.": "c",
        "-..": "d",
        ".": "e",
        "..-.": "f",
        "--.": "g",
        "....": "h",
        "..": "i",
        ".---": "j",
        "-.-": "k",
        ".-..": "l",
        "--": "m",
        "-.": "n",
        "---": "o",
        ".--.": "p",
        "--.-": "q",
        ".-.": "r",
        "...": "s",
        "-": "t",
        "..-": "u",
        "...-": "v",
        ".--": "w",
        "-..-": "x",
        "-.--": "y",
        "--..": "z",
        ".----": "1",
        "..---": "2",
        "...--": "3",
        "....-": "4",
        ".....": "5",
        "-....": "6",
        "--...": "7",
        "---..": "8",
        "----.": "9",
        "-----": "0",
        "--..--": ",",
        ".-.-.-": ".",
        "..--..": "?",
        "-..-.": "/",
        "-....-": "-",
        "-.--.": "(",
        "-.--.-": ")",
        ".-...": "&",
        ".--.-.": "@",
        "-.-.--": "!",
        "...-..-": "$",
        ".-.-.": "%",
        "-...-": "=",
        ".-.-.": "+",
        "..--.-": "_",
        ".-..-.": '"',
        ".-.-": "<",
        ".-..-.": ">",
        "---...": ":",
        "-.-.-.": ";",
        "/": " ",
    }
    message = message.replace(" ", "/").replace("_", "/")
    return "".join([morse_code[letter] for letter in message.lower()])
__all__ = ['encode', 'decode']