
def encrypt(plaintext, key):
    plaintext = plaintext.lower()
    ciphertext = ""
    i = 0
    alphabet_start = 97
    alphabet_end = 122
    for char in plaintext:
        if ord(char) < alphabet_start or ord(char) > alphabet_end:
            continue

        if i == len(key):
            i = 0

        val = ((ord(char) + ord(key[i])) % alphabet_start) + alphabet_start

        if val > alphabet_end:
            val = alphabet_start + (val - alphabet_end - 1)

        ciphertext += chr(val)
        i += 1

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
