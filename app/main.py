from cipher import VigenereCipher
import numpy as np

v_cipher = VigenereCipher()
ciphertext = v_cipher.encrypt("attackatdawn")
print(ciphertext)
plaintext = v_cipher.decrypt(ciphertext)
