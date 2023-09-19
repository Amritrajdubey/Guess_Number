import random

def guess_number(x):
    random_number = random.randint(1,x)
    count = 0

    while count < 3:
        guess = int(input(f'Guess a random number between 1 and {x}: '))
        count += 1

        if guess < random_number:
            print(f'Sorry guess again ,number is low')
        elif guess > random_number:
            print(f'Sorry guess again ,number is high')

    if guess == random_number:
        print(f'Hurray , Congrats you guessed {random_number} which is right in {count} turn')
    else:
        print('Close but not accurate ,Try again')

guess_number(10)