import random

print('This is a number guessing game!')
play = True
while play:
    random_number = random.randint(0,10)
    #random_number = 6
    remaing_guesses = 5
    while remaing_guesses != 0:
        guess = input('Input your guess bewtween 0 and 10: ')
        number_guess = int(guess)
        if number_guess == random_number:
            print('That was correct, you win!')
            break
        elif number_guess > random_number:
            print('Your guess is to high')
            remaing_guesses -=1
            print(f'{remaing_guesses} guesses left!')
        elif number_guess < random_number:
            print('Your guess is too low')
            remaing_guesses -=1
            print(f'{remaing_guesses} guesses left!')
    if remaing_guesses == 0:
        print('Sorry you ran out of guesses')
        print(f'The correct number was {random_number}')
    play_again = 'y'
    play_again_answer = input('Would you like to play again (y or n): ')
    if play_again == play_again_answer.lower():
        remaing_guesses = 0
    else:
        break
        



