"""Основная рабочая программа"""
from utils import load_random_word
from player import Player

"""Прорамма узнает имя игрока и приветствует его"""
player_name = input('Введите имя игрока:')
print(f'Привет, {player_name}!')

"""Идет подготовка к основному коду
создается экземпляр класса Player
а также выберается случайное искомое слово"""
player = Player(player_name, [])
path = 'words.json'
basic_word = load_random_word(path)
print(f'''Составьте {basic_word.count_subwords()} слов из слова {basic_word.word}
Слова должны быть не короче 3 букв
Чтобы закончить игру, угадайте все слова или напишите "stop"''')

print(f'Поехали, ваше первое слово?')


"""Основной цикл программы"""
while player.count_words() < basic_word.count_subwords():
    answer = str(input())
    """Стоп-слово прекращает игру и выводит результат"""
    if answer.lower() == 'stop' or answer.lower() == 'стоп':
        break
    elif len(answer) < 3:
        print('слишком короткое слово')
    elif basic_word.has_word(answer) == False:
        print('неверно')
    elif player.has_word(answer):
        print('уже использовано')
    else:
        print('верно')
        player.add_word(answer)

"""По завершению цикла программа выводит результат"""
print(f'Игра завершена, вы угадали {player.count_words()} слов!')
