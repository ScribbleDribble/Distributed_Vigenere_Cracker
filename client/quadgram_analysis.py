
class QuadgramAnalyzer(object):

    def __init__(self):
        self.quadgram_table = {}
        self.sum_quadgrams = 0
        self.read_data()

    def read_data(self):
        with open("english_quadgrams.txt", "r") as file:

            for line in file.readlines():
                line_content = line.split(" ")
                self.quadgram_table[line_content[0]] = int(line_content[1])
                self.sum_quadgrams += int(line_content[1])

            file.close()

    def log_probability(self, quadgram):
        import math
        if quadgram in self.quadgram_table:
            return math.log10(self.quadgram_table[quadgram]/self.sum_quadgrams)

        else:
            return 0

    def text_fitness(self, text):
        text = text.upper()
        ngram_size = 4
        i = 0
        p = 0
        while i + ngram_size <= len(text):
            # since log(a*b) = log(a) + log(b) instead of p(a)*p(b)
            p += self.log_probability(text[i: i + ngram_size])
            i += 1
        return p

