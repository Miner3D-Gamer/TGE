import re
def decode(text: str) -> str:
    """
    Decode HTML-encoded characters in the given text.

    This function takes a string containing HTML-encoded characters and replaces them
    with their corresponding decoded characters. It supports a predefined set of special
    HTML-encoded characters.

    Args:
        text (str): The input text containing HTML-encoded characters.

    Returns:
        str: The input text with HTML-encoded characters replaced by their decoded counterparts.
    """
    special_encoding = [
        "&Agrave;",
        "&Aacute;",
        "&Acirc;",
        "&Atilde;",
        "&Auml;",
        "&Aring;",
        "&agrave;",
        "&aacute;",
        "&acirc;",
        "&atilde;",
        "&auml;",
        " &aring;",
        "&AElig;",
        "&aelig;",
        "&szlig;",
        "&Ccedil;",
        "&ccedil;",
        "&Egrave;",
        "&Eacute;",
        "&Ecirc;",
        "&Euml;",
        "&egrave;",
        "&eacute;",
        "&ecirc;",
        "&euml;",
        "&#131;",
        "&Igrave;",
        "&Iacute;",
        "&Icirc;",
        "&Iuml;",
        "&igrave;",
        "&iacute;",
        "&icirc;",
        "&iuml;",
        "&Ntilde;",
        "&ntilde;",
        "&Ograve;",
        "&Oacute;",
        "&Ocirc;",
        "&Otilde;",
        "&Ouml;",
        "&ograve;",
        "&oacute;",
        "&ocirc;",
        "&otilde;",
        "&ouml;",
        "&Oslash;",
        "&oslash;",
        "&#140;",
        "&#156;",
        "&#138;",
        "&#154;",
        "&Ugrave;",
        "&Uacute;",
        "&Ucirc;",
        "&Uuml;",
        "&ugrave;",
        "&uacute;",
        "&ucirc;",
        "&uuml;",
        "&#181;",
        "&#215;",
        "&Yacute;",
        "&#159;",
        "&yacute;",
        "&yuml;",
        "&#176;",
        "&#134;",
        "&#135;",
        "&lt;",
        "&gt;",
        "&#177;",
        "&#171;",
        "&#187;",
        "&#191;",
        "&#161;",
        "&#183;",
        "&#149;",
        "&#153;",
        "&copy;",
        "&reg;",
        "&#167;",
        "&#182;",
    ]
    special_character = [
        "À",
        "Á",
        "Â",
        "Ã",
        "Ä",
        "Å",
        "à",
        "á",
        "â",
        "ã",
        "ä",
        "å",
        "Æ",
        "æ",
        "ß",
        "Ç",
        "ç",
        "È",
        "É",
        "Ê",
        "Ë",
        "è",
        "é",
        "ê",
        "ë",
        "ƒ",
        "Ì",
        "Í",
        "Î",
        "Ï",
        "ì",
        "í",
        "î",
        "ï",
        "Ñ",
        "ñ",
        "Ò",
        "Ó",
        "Ô",
        "Õ",
        "Ö",
        "ò",
        "ó",
        "ô",
        "õ",
        "ö",
        "Ø",
        "ø",
        "Œ",
        "œ",
        "Š",
        "š",
        "Ù",
        "Ú",
        "Û",
        "Ü",
        "ù",
        "ú",
        "û",
        "ü",
        "µ",
        "×",
        "Ý",
        "Ÿ",
        "ý",
        "ÿ",
        "°",
        "†",
        "‡",
        "<",
        ">",
        "±",
        "«",
        "»",
        "¿",
        "¡",
        "·",
        "•",
        "™",
        "©",
        "®",
        "§",
        "¶",
    ]

    # Use regex to find HTML-encoded characters within the text
    encoded_chars = re.findall("&\w+;", text)

    # Iterate over the found encoded characters and replace them with decoded counterparts
    for encoded_char in encoded_chars:
        if encoded_char in special_encoding:
            index = special_encoding.index(encoded_char)
            decoded_char = special_character[index]
            text = text.replace(encoded_char, decoded_char)

    return text


def encode(text: str) -> str:
    """
    Encodes special characters in the input text into their corresponding HTML character entities.

    This function takes a string as input and replaces specific special characters with their equivalent
    HTML character entity codes. The conversion includes characters like accented letters, symbols, and
    other non-standard characters commonly used in text.

    Args:
        text (str): The input text containing special characters to be encoded.

    Returns:
        str: The input text with special characters replaced by their corresponding HTML character entities.
    """
    special_encoding = [
        "&Agrave;",
        "&Aacute;",
        "&Acirc;",
        "&Atilde;",
        "&Auml;",
        "&Aring;",
        "&agrave;",
        "&aacute;",
        "&acirc;",
        "&atilde;",
        "&auml;",
        " &aring;",
        "&AElig;",
        "&aelig;",
        "&szlig;",
        "&Ccedil;",
        "&ccedil;",
        "&Egrave;",
        "&Eacute;",
        "&Ecirc;",
        "&Euml;",
        "&egrave;",
        "&eacute;",
        "&ecirc;",
        "&euml;",
        "&#131;",
        "&Igrave;",
        "&Iacute;",
        "&Icirc;",
        "&Iuml;",
        "&igrave;",
        "&iacute;",
        "&icirc;",
        "&iuml;",
        "&Ntilde;",
        "&ntilde;",
        "&Ograve;",
        "&Oacute;",
        "&Ocirc;",
        "&Otilde;",
        "&Ouml;",
        "&ograve;",
        "&oacute;",
        "&ocirc;",
        "&otilde;",
        "&ouml;",
        "&Oslash;",
        "&oslash;",
        "&#140;",
        "&#156;",
        "&#138;",
        "&#154;",
        "&Ugrave;",
        "&Uacute;",
        "&Ucirc;",
        "&Uuml;",
        "&ugrave;",
        "&uacute;",
        "&ucirc;",
        "&uuml;",
        "&#181;",
        "&#215;",
        "&Yacute;",
        "&#159;",
        "&yacute;",
        "&yuml;",
        "&#176;",
        "&#134;",
        "&#135;",
        "&lt;",
        "&gt;",
        "&#177;",
        "&#171;",
        "&#187;",
        "&#191;",
        "&#161;",
        "&#183;",
        "&#149;",
        "&#153;",
        "&copy;",
        "&reg;",
        "&#167;",
        "&#182;",
    ]
    special_character = [
        "À",
        "Á",
        "Â",
        "Ã",
        "Ä",
        "Å",
        "à",
        "á",
        "â",
        "ã",
        "ä",
        "å",
        "Æ",
        "æ",
        "ß",
        "Ç",
        "ç",
        "È",
        "É",
        "Ê",
        "Ë",
        "è",
        "é",
        "ê",
        "ë",
        "ƒ",
        "Ì",
        "Í",
        "Î",
        "Ï",
        "ì",
        "í",
        "î",
        "ï",
        "Ñ",
        "ñ",
        "Ò",
        "Ó",
        "Ô",
        "Õ",
        "Ö",
        "ò",
        "ó",
        "ô",
        "õ",
        "ö",
        "Ø",
        "ø",
        "Œ",
        "œ",
        "Š",
        "š",
        "Ù",
        "Ú",
        "Û",
        "Ü",
        "ù",
        "ú",
        "û",
        "ü",
        "µ",
        "×",
        "Ý",
        "Ÿ",
        "ý",
        "ÿ",
        "°",
        "†",
        "‡",
        "<",
        ">",
        "±",
        "«",
        "»",
        "¿",
        "¡",
        "·",
        "•",
        "™",
        "©",
        "®",
        "§",
        "¶",
    ]

    # Iterate over the special characters and replace them with their encoded counterparts
    for encoding, character in zip(special_encoding, special_character):
        text = text.replace(character, encoding)

    return text
