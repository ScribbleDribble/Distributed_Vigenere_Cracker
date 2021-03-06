from quadgram_analysis import QuadgramAnalyzer


def init(ciphertext, key_length):
    text_groups = caesar_groups(ciphertext, key_length)
    candidate_letters = frequency_analyzer(key_length, text_groups)
    keys = generate_keys(candidate_letters)
    q = QuadgramAnalyzer()
    return evaluate_keys(q, ciphertext, keys)


def caesar_groups(ciphertext, key_length):
    text_group_str = ["" for i in range(key_length)]
    count = 0
    for i, char in enumerate(ciphertext):
        text_group_str[count] += char
        count += 1
        if count == key_length:
            count = 0

    return text_group_str


def frequency_analyzer(key_length, text_groups):
    # work around for importing with dispy
    import cipher
    alphabet_freq_table = [8.12, 1.49, 2.71, 4.32, 12.02, 2.3, 2.03, 5.92, 7.31, 0.1, 0.69, 3.98, 2.61, 6.95, 7.68,
                           1.82, 0.11, 6.02, 6.28, 9.1, 2.88, 1.11, 2.09, 0.17, 2.11, 0.07]
    alphabet_start = 97
    scores = []

    candidate_letters = [[] for i in range(key_length)]

    for group_num, group in enumerate(text_groups):
        for i in range(26):
            deciphered = cipher.decrypt_unknown_key(group, chr(alphabet_start + i))
            score = 0
            for letter in deciphered:
                score += alphabet_freq_table[ord(letter) % alphabet_start]

            scores.append((score, chr(alphabet_start + i)))

        scores.sort(reverse=True)
        for i, score in enumerate(scores):
            if i == 4:
                break
            candidate_letters[group_num].append(score[1])

        scores = []

    return candidate_letters


def generate_keys(candidate_letters):
    import itertools
    cartesian_product = list(itertools.product(*candidate_letters))
    keys = []
    key = ""
    for key_tuple in cartesian_product:
        for char in key_tuple:
            key += char

        keys.append(key)
        key = ""

    return keys


def sort_score(score):
    return score[1]


def evaluate_keys(analyzer, ciphertext, keys):
    import cipher
    fitness = []
    for key in keys:
        text = cipher.decrypt(ciphertext, key)
        score = analyzer.text_fitness(text)

        fitness.append((key, score, text))

    fitness.sort(reverse=True, key=sort_score)
    return fitness[:5]
