'''
ERIC LEIGH
31 MAY 2019
NUMBER GUESSING GAME
'''
import random

guesses = 0
number = random.randint(1, 10)
print('Welcome to the Game')
print('Guess the number I am thinking of between 1 and 10')
print('You have 5 guesses, good luck!')
while guesses < 5:
    print('Guess a number please:')
    guess = input()
    guess = int(guess)

    guesses = guesses + 1

    if guess > number:
        print('Your guess is too high')
        continue
    if guess < number:
        print('Your guess is too low')
        continue
    if guess == number:
       print('You guessed the number!')        
       break
print('No please try the game again!')