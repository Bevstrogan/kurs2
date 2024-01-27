
from utils import load_random_word
from player import Player
player_name = input('Введите имя игрока:')
print(f'Привет, {player_name}!')
player = Player(player_name, [])
path = 'words.json'
basic_word = load_random_word(path)
print(f'''Составьте {basic_word.count_subwords()} слов из слова {basic_word.word}
Слова должны быть не короче 3 букв
Чтобы закончить игру, угадайте все слова или напишите "stop"''')

print(f'Поехали, ваше первое слово?')
print(basic_word.subwords)

while player.count_words() < basic_word.count_subwords():
    answer = str(input())
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



print(f'Игра завершена, вы угадали {player.count_words()} слов!')