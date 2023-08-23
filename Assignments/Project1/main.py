import random

random_number = random.randint(1, 100)

count = 1

while True:
    x = int(input('Choose Your Number: '))
    if x < random_number:
        count += 1
        print('Up')
    elif x > random_number:
        count += 1
        print('Down')
    if x == random_number:
        print('You make it! the number is %d and you try %dtimes.' % (x, count))
        break
