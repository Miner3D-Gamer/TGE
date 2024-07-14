from random import shuffle
from hashlib import sha256

def get_hello_world(reminder_start:int=10000, reminder_every:int=10):
    THIS_IS_IT_I_PROMISE =b'\x7f\x83\xb1e\x7f\xf1\xfcS\xb9-\xc1\x81H\xa1\xd6]\xfc-K\x1f\xa3\xd6w(J\xdd\xd2\x00\x12m\x90i'

    def scramble_word(word):

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

def print_hello_world():
    print("%s in %s attempts"%get_hello_world(reminder_start=-1))