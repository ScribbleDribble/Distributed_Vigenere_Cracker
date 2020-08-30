import cipher
import crack

ciphertext = cipher.encrypt("His start-up Neuralink applied to launch human trials last year"
                            "The interface could allow people with neurological conditions to control phones or computers with their mind."
                            "Mr Musk argues such chips could eventually be used to help cure conditions such as dementia, Parkinson's disease and spinal cord injuries", "irons")
print(ciphertext)
plaintext = cipher.decrypt(ciphertext, "irons")
print(plaintext)

candidates = crack.init(ciphertext, 5)
print(candidates)

