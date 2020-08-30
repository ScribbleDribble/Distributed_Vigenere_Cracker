import numpy as np


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


def encrypt(plaintext, key):
    v_table = init_table()
    plaintext = plaintext.lower()
    alphabet_start = 97
    alphabet_end = 122
    j = 0
    key_pass = 1
    ciphertext = ""

    i = 0
    for letter in plaintext:
        if ord(letter) < alphabet_start or ord(letter) > alphabet_end:
            continue

        if i >= len(key) * key_pass:
            j = 0
            key_pass += 1

        ciphertext += v_table[ord(letter) - alphabet_start, ord(key[j]) - alphabet_start]
        i += 1
        j += 1

    return ciphertext.upper()


def decrypt(ciphertext, key):
    # note: it doesn't work with any punctuation
    ciphertext = ciphertext.lower()

    alphabet_start = 97
    alphabet_size = 26
    i = 0
    plaintext = ""
    j = 0
    while i < len(ciphertext):
        if j >= len(key):
            j = 0

        # must find difference in index rightward of row value
        if ord(key[j]) > ord(ciphertext[i]):
            diff = alphabet_size - (ord(key[j]) - ord(ciphertext[i]))
        else:
            diff = abs(ord(key[j]) - ord(ciphertext[i]))

        j += 1
        i += 1
        plaintext += chr(diff + alphabet_start)

    return plaintext


def decrypt_unknown_key(ciphertext, key):
    ciphertext = ciphertext.lower()

    alphabet_start = 97
    alphabet_size = 26
    i = 0
    plaintext = ""
    j = 0
    while i < len(ciphertext):
        # must find difference in index rightward of row value
        if ord(key) > ord(ciphertext[i]):
            diff = alphabet_size - (ord(key) - ord(ciphertext[i]))
        else:
            diff = abs(ord(key) - ord(ciphertext[i]))

        i += 1
        plaintext += chr(diff + alphabet_start)

    return plaintext
