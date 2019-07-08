#random number generator
import random
number=random.randint(1,100)

#define variables.  
TOP_NUM=100
MAXGUESS=10
guesscount=0

#game rules
print("Welcome to the Number Guessing Game...")
print("I'm thinking of a number between 1 and", TOP_NUM,". You have", MAXGUESS,"chances to figure it out."  )

#collect information
while guesscount <= MAXGUESS:
	print("What do you guess?")
	guesscount = guesscount + 1
	guess = input()
	guess = int(guess)
	#if guess > TOP_NUM
	#	print("please choose a number between 1 and", TOP_NUM,")
	if guess > TOP_NUM:
		print("please guess a number between 1 and", TOP_NUM)
	elif guess < 1:
		print("please guess a number between 1 and", TOP_NUM)
	elif guess < number:
		print("I will give you a hint, your guess is too low")
	elif guess > number: 
		print("I will give you a hint, your guess is too high")
	elif guess == number:
		break
if guesscount > MAXGUESS:
	print("I am sorry but you have exceeded your guess count, the number I was thinking of was", number)
if guess == number:
	print("Great job!, you have guessed my number")





	


