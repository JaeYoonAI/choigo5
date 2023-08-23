import random

rsp = ['Rock', 'Scissors', 'Paper']

a = input(
    'This is Rock Scissors Paper Game. Do you want to play the game or not? (Y/N): ').lower()

w = 0
l = 0
d = 0

if a == 'y':
    while True:
        computer = random.choice(rsp).lower()
        x = input('Choose one (Rock, Scissors, Paper): ').lower()
        while computer == 'rock':
            if x == 'scissors':
                print('Lose.')
                l += 1
            if x == 'paper':
                print('Win')
                w += 1
            if x == computer:
                print('Draw.')
                d += 1
            else:
                print('Wrong Input')
            break
        while computer == 'paper':
            if x == 'scissors':
                print('Win.')
                w += 1
            if x == 'rock':
                print('Lose.')
                l += 1
            if x == computer:
                print('Draw.')
                d += 1
            else:
                print('Wrong Input')
            break
        while computer == 'scissors':
            if x == 'paper':
                print('Lose.')
                l += 1
            if x == 'rock':
                print('Win.')
                w += 1
            if x == computer:
                print('Draw.')
                d += 1
            else:
                print('Wrong Input')
            break
        a = input(
            'Continue? (Y/N): ').lower()
        if a == 'y':
            continue
        if a == 'n':
            break


if a == 'n':
    print('Game Over')
    print('Win: %d, Lose: %d, Draw: %d' % (w, l, d))
