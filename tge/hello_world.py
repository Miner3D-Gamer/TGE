from random import shuffle
from hashlib import sha256
from typing import Tuple

__all__ = ["get_hello_world", "print_hello_world"]

def get_hello_world(reminder_start: int = 10000, reminder_every: int = 10)-> Tuple[str, int]:
    """
    Generates a "Hello World" string return it.

    Args:
        reminder_start (int, optional): The initial interval for attempt reminders. Defaults to 10000.
        reminder_every (int, optional): The frequency (in attempts) at which reminders are printed. Defaults to 10.

    Returns:
        tuple: A tuple containing:
            - str: "Hello World".
            - int: The number of attempts taken to find "Hello World".
    """
    THIS_IS_IT_I_PROMISE = b'\x7f\x83\xb1e\x7f\xf1\xfcS\xb9-\xc1\x81H\xa1\xd6]\xfc-K\x1f\xa3\xd6w(J\xdd\xd2\x00\x12m\x90i'

    def scramble_word(word: str):
        """
        Scrambles the characters of the given word by shuffling them.

        Args:
            word (str): The word to scramble.

        Returns:
            str: The scrambled word.
        """
        word_list = list(word)
        shuffle(word_list)
        return ''.join(word_list)

    attempts = 0
    reminders = reminder_start
    while True:
        attempts += 1
        if attempts % reminders == reminder_every:
            print(f"At {attempts} attempts")
            reminders *= 10
        scram = scramble_word("Hell oWl!dor")
        if sha256(scram.encode()).digest() == THIS_IS_IT_I_PROMISE:
            break
    return scram, attempts


def print_hello_world()-> None:
    """
    Prints the result of `get_hello_world`.

    Calls `get_hello_world` with a reminder interval of -1 (no reminders) and prints the formatted result.
    """
    print("%s in %s attempts" % get_hello_world(reminder_start=-1))