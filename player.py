"""Класс направленный на введенные пользователем слова"""
class Player():
    def __init__(self, name: str, used_subwords: list):
        self.name = name
        self.used_subwords: list = used_subwords

    """Функция считает кол-во введенных пользователем
    правильных слов"""
    def count_words(self):
        return len(self.used_subwords)

    """Функция добавляем слово к списку использованных слов"""
    def add_word(self, word):
        self.used_subwords.append(word)

    """функция проверяет былоли использованно раннее введенное пользователем слово"""
    def has_word(self, word):
        return word in self.used_subwords
