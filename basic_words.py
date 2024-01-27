class BasicWord():
    def __init__(self, word: str, subwords: list):
        self.word = word
        self.subwords = subwords

    def count_subwords(self):
        return len(self.subwords)

    def has_word(self, player_word):
        return player_word in self.subwords
