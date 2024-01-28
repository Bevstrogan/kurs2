"""Функция направленна на проверку введенного игроком слова"""
class BasicWord():
    def __init__(self, word: str, subwords: list):
        self.word = word
        self.subwords = subwords


"""Функция выводит кол-во слов, которых можно собрать из исходного слова"""
    def count_subwords(self):
        return len(self.subwords)
        
"""Функция проверяет есть ли введенное слово в списк ответов"""
    def has_word(self, player_word):
        return player_word in self.subwords
