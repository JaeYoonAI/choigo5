import random

rsp = ['rock', 'scissors', 'paper']

a = input(
    'This is Rock Scissors Paper Game. Do you want to play the game or not? (Y/N): ').lower()

w = 0
l = 0
d = 0

if a == 'y':
    while True:
        computer = random.choice(rsp).lower()
        x = input(
            'Choose one (Rock, Scissors, Paper) or quit the game?(q): ').lower()
        if x == 'q':
            break
        # inserting q position is important!
        if x not in rsp:
            print('Wrong Input')
            continue
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
            break


print('Game Over')
print(f'Win: {w}, Lose: {l}, Draw: {d}')
