import numpy as np


class VigenereCipher:

    def __init__(self, key="lemon"):
        self.key = key.lower()
        self.v_table = VigenereCipher.init_table()

    @staticmethod
    def init_table():
        alphabet_size = 26
        alphabet_start = 97
        alphabet_end = 122
        row = 0
        v_table = np.zeros([alphabet_size, alphabet_size], dtype="str")
        i = alphabet_start
        while row < alphabet_size:
            temp = []
            letter_count = 0
            while letter_count < alphabet_size:
                if i > alphabet_end:
                    i = alphabet_start + i - alphabet_end - 1
                temp.append(chr(i))
                letter_count += 1
                i += 1

            v_table[row:] = temp
            row += 1
            i = alphabet_start + row

        return v_table

    def encrypt(self, plaintext):
        plaintext.lower()
        alphabet_start = 97
        j = 0
        key_pass = 1
        ciphertext = ""
        for i, letter in enumerate(plaintext):
            if i >= len(self.key) * key_pass:
                j = 0
                key_pass += 1

            ciphertext += self.v_table[ord(letter) - alphabet_start, ord(self.key[j]) - alphabet_start]
            j += 1

        return ciphertext.upper()

    def decrypt(self, ciphertext):
        ciphertext = ciphertext.lower()
        alphabet_start = 97
        alphabet_size = 26
        i = 0
        key_pass = 1

        plaintext = ""
        j = 0
        while i < len(ciphertext):
            if j >= len(self.key):
                # key_pass += 1
                j = 0

            if ord(self.key[j]) > ord(ciphertext[i]):
                diff = alphabet_size - (ord(self.key[j]) - ord(ciphertext[i]))
            else:
                diff = abs(ord(self.key[j]) - ord(ciphertext[i]))

            j += 1
            i += 1
            plaintext += chr(diff + alphabet_start)

        return plaintext
    