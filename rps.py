import random
import time

def print_dramatic_text(text: str, delay=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

if __name__ == '__main__':
    print_dramatic_text('welcome to rock, paper, scissors! 🗿📃✂️')

    options = ['rock', 'paper', 'scissors']
    choices = random. randint (0, 2)

    # print('computer player selected: ' + options[choices])
    computer = options[choices]

    player = input('enter your choice (rock, paper, scissors): ')
    while player != 'rock' and player != 'paper' and player != 'scissors':
       player = input('please choose rock, paper, or scissors:')
                        
    print(f'player selected: {player}')

    if player == 'rock' and computer ==  'rock':
        print('it\'s a tie!')
    if player == 'rock' and computer ==  'paper':
        print('you lose!')
    if player == 'rock' and computer ==  'scissors':
        print('you win!')

    if player == 'scissors' and computer ==  'rock':
        print('you lose!')
    if player == 'scissors' and computer ==  'paper':
        print('you win!')
    if player== 'scissors' and computer == 'scissors':
        print('it\'s a tie!')

    
    if player == 'paper' and computer ==  'rock':
        print('you win!')
    if player == 'paper' and computer == 'scissors':
        print('you lose!')
    if player == 'paper' and computer == 'paper':
        print('it\'s a tie!')

