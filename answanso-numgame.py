#!/usr/bin/python
# random number generator
# Anthony  Swanson

# import libs for game
import random


# define vars
mysterynum_var = random.randint(1,50)
loop_var = 0

# welcome screen
print('######################################################')
print('#                                                    #')
print('#                                                    #')
print('#        Welcome to the Number Guessing Game.        #')
print('#         Guess a number between 1 and 50...         #')
print('#               You have 10 attempts!                #')
print('#                                                    #')
print('#                                           v0.1     #')
print('######################################################')
print('')
# start game

while loop_var < 10:
    guessnum_var = input('> ')
    if guessnum_var != mysterynum_var:
        print('Wrong number, guess again!')
        loop_var = loop_var + 1
    elif guessnum_var == mysterynum_var:
        print('You guessed correctly!')
        break
while loop_var == 10:
    print('')
    print('Sorry, you ran out of attempts...')
    break
