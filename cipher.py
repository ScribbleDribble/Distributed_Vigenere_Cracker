import numpy as np


class VigenereCipher:

    def __init__(self):
        self.key = "LEMON"
        alphabet_size = 26
        alphabet_start = 97
        alphabet_end = 122
        row = 0
        v_table = np.zeros([26, 26], dtype="str")
        i = alphabet_start
        while row < alphabet_size:
            temp = []
            letter_count = 0
            while letter_count < alphabet_size:
                if i > alphabet_end:
                    i = alphabet_start + i - alphabet_end + 1
                temp.append(chr(i))
                letter_count += 1
                i += 1

            v_table[row:] = temp
            row += 1
            i = alphabet_start + row


    @staticmethod
    def encrypt():
        return
