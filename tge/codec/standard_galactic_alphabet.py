def encode(text: str) -> str:
    """
    Encodes a string by replacing each character with a corresponding symbol from a predefined table.

    Args:
        text (str): The input string to be encoded.

    Returns:
        str: The encoded string with characters replaced by symbols.

    Notes:
        Characters not found in the encoding table remain unchanged.
    """
    table = {
        "a": "ᔑ",
        "b": "ܠ",
        "c": "i",
        "d": "↸",
        "e": "ᒷ",
        "f": "⎓",
        "g": "├",
        "h": "₸",
        "i": "╎",
        "j": "⋮",
        "k": "ꖌ",
        "l": "|:",
        "m": "٦",
        "n": "リ",
        "o": "フ",
        "p": "¡ǃ",
        "q": "ᑖ",
        "r": "∴",
        "s": "߆",
        "t": "ℸ ̣",
        "u": "⚍",
        "v": "⍊",
        "w": "∷",
        "x": "˙̸ ",
        "y": "॥",
        "z": "⋂",
        "1": "⥍",
        "2": "∠",
        "3": ">",
        "4": "⊐",
        "5": "ⵎ",
        "6": "X",
        "7": "Δ",
        "8": "⎕",
        "9": "┌┐",
        "0": "└┘",
    }
    return "".join(table.get(char, char) for char in text)


def decode(text: str) -> str:
    """
    Decodes a string by replacing each symbol with the corresponding character from a predefined table.

    Args:
        text (str): The encoded string to be decoded.

    Returns:
        str: The decoded string with symbols replaced by characters.

    Notes:
        Symbols not found in the decoding table remain unchanged.
    """
    table = {
        "ᔑ": "a",
        "ܠ": "b",
        "i": "c",
        "↸": "d",
        "ᒷ": "e",
        "⎓": "f",
        "├": "g",
        "₸": "h",
        "╎": "i",
        "⋮": "j",
        "ꖌ": "k",
        "|:": "l",
        "٦": "m",
        "リ": "n",
        "フ": "o",
        "¡ǃ": "p",
        "ᑖ": "q",
        "∴": "r",
        "߆": "s",
        "ℸ ̣": "t",
        "⚍": "u",
        "⍊": "v",
        "∷": "w",
        "˙̸ ": "x",
        "॥": "y",
        "⋂": "z",
        "⥍": "1",
        "∠": "2",
        ">": "3",
        "⊐": "4",
        "ⵎ": "5",
        "X": "6",
        "Δ": "7",
        "⎕": "8",
        "┌┐": "9",
        "└┘": "0",
    }
    return "".join(table.get(char, char) for char in text)
__all__ = ['encode', 'decode']