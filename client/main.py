import cipher
import crack
import time
start_time = time.time()

ciphertext = cipher.encrypt("His start-up Neuralink applied to launch human trials last year"
                            "The interface could allow people with neurological conditions to control phones or computers with their mind."
                            "Mr Musk argues such chips could eventually be used to help cure conditions such as dementia, Parkinson's disease and spinal cord injuries", "network")
print(ciphertext)
# plaintext = cipher.decrypt(ciphertext, "irons")
# print(plaintext)

candidates = crack.init(ciphertext, 7)
print(f"--- {time.time() - start_time} seconds ---")
print(candidates)

