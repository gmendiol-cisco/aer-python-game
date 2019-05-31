###############################
##### Tracking changes
#####  1.  Adding verifcation of user input 02 May 2019
#####   and commented out showing the answer
#####

#import library to generate random number between 1 and 100
from random import randint 

#print("Start of Game")
guess_count = 0
user_guess = 50
TOP_NUM =100
MAXGUESS = 10
#print (MAXGUESS)

GAMENUM = randint(1,TOP_NUM)
    
#print (GAMENUM)

print("Welcome to the Number Guessing Game...")
print("I'm thinking of a number between 1 and", TOP_NUM, ". You have", MAXGUESS,"chances to figure it out."  )


while guess_count <= MAXGUESS:
#indentation is important and signifies what is "inside" the loop
   
   #Ask user for first guess
   print("What is your guess?")
   
   #get input from keyboard, type cast it to an int from a string
   user_guess = int(input())
   
   while (user_guess > TOP_NUM) or (user_guess < 1):
      print("Your answer is out of range.  Try again")
      user_guess = int(input())
      guess_count += 1
   #end while loop

   #increase the guess_count
   guess_count += 1

   #Check if their number
   
   if user_guess == GAMENUM:
      #if yes issue congratulations and tell them how many guesses they needed      
      print("Congratulations, you got it in", guess_count,"tries.")
      break #exit while loop
   
   elif guess_count == MAXGUESS:
      print ("That was wrong too. Sorry you ran out of guesses.  Better luck next time.")
      break #exit while loop
   
   else:
      print("Nope not it...try again.")

#end of the while loop