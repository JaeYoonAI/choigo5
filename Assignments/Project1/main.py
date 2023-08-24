import random

max_try = 0

while True:
    random_number = random.randint(1, 100)
    print(f'Your highst try number is {max_try}')

    count = 0

    # I add 'count += 1' on if and elif but change to outside of if and elif so the count start with '0'

    while True:
        x = int(input('Choose Your Number(1~100): '))
        if x > 100 or x < 1:
            print('Please enter the number between 1-100')
            continue
        count += 1
        if x < random_number:
            print('Up')
        elif x > random_number:
            print('Down')
        if x == random_number:
            print(
                f'You make it! the number is {random_number} and you try {count}times.')
            if count > max_try:
                max_try = count
            break

    will_continue = input('continue?(y/n): ')
    if will_continue == 'y':
        continue
    if will_continue == 'n':
        break
