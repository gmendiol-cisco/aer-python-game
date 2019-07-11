'''
Klear, Scott
04 JUNE 2019
Purpose: Simulate a random number game to practice python scripting
'''

#Instructions: Come up with a random number game and based on the number inputs specific things happen, use while, for, and ifs
import random

#Generate a random number between 1 and 10
r = random.randint(1,10)

#Welcome to my cool game
print('Welcome to the random number game!!!')
print()

#Explain the instructions
print('The instructions are easy, enter guess the random number and the game will reward you with motivational speaches.')
print()

#Start initial loop to give 5 guesses
attempt = 0

while attempt < 5 :
    #LOOP: Check for valid input
    x = 0
    while x <= 5 :
        #Check for idiots that cannot follow directions, print/exit if attempts is greater than 5
        if x == 5 :
            print('Your a dumbass, game over!')
            exit()

        #Request input for a number between 1 and 10
        y = input('Try to guess my random number between 1 and 10: ')

        #Check for integer, terminate if not.
        try :
            val = int(y)
        except ValueError :
            print("That wasn't a number idiot")
            exit()

        y = int(y)
        #Check for between 1 and 10
        if y < 1 :
            print('Your number is to small, try again!')
        elif y > 10 :
            print('Your number is to big, try again!')
        else :
            break

        #Increment X
        x += 1

    #Check if input number is correct and print motivational speach, if they don't get it correct ask to do it again
    if r == y :
        print('BOOM! You Got It! The mystery prize is a big box of NOTHING!')
        exit()
    elif r == (y + 1) or r == (y - 1) :
        answer = input('You were so close, but still a failure! Would you like to try again? (Y/N): ')
        if answer in ('n','N','No','NO','no') :
            print('Thanks and have a nice day!')
            exit()
    else :
        answer = input('Complete Failure Dude. Would you like to try again? (Y/N): ')
        if answer in ('n','N','No','NO','no') :
            print('Thanks and have a nice day!')
            exit()
    attempt += 1

print('Oh No! You ran out of guesses! Thanks for trying!')