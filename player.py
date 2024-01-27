class Player():
    def __init__(self, name: str, used_subwords: list):
        self.name = name
        self.used_subwords: list = used_subwords

    def count_words(self):
        return len(self.used_subwords)

    def add_word(self, word):
        self.used_subwords.append(word)

    def has_word(self, word):
        return word in self.used_subwords
