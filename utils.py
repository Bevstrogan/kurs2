import random
import json
from basic_words import BasicWord

"""Функция направленна на получение списка с словами 
и выбора случаййного исходного слова              """

#Возникли проблемы с request. Из-за этого сделал на json
def load_random_word(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        json_file = json.load(file)
        random_word = random.choice(json_file)
        return BasicWord(word=random_word['word'], subwords=random_word['subwords'])
