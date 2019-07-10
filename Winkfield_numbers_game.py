#!/usr/bin/python

#Defining varibles
correct_answer = 50
max_attempts = 3
attempts = 0 

#Initial Welcome statement  
print("Welcome to the numbers game.\n")

#for loop to track number of attempts
for attempts in range(max_attempts):
    print("You are on attempt " + str(attempts + 1))
    #Ask for number to guess?
    myInput = raw_input("Guess the number from 1 - 100: ")
    
    #Make sure converted to number
    try:
        int(myInput)
    except ValueError:
        print("Thats not a number dummy!!!")
        quit()

    #if statement to determine correct or not
    if (correct_answer == int(myInput)):
        print("YOU WIN!!!")
        quit()
    else:
        if  (correct_answer > int(myInput)):
            print("TOO LOW HOMEY!!!")
        else:
            print("TOO HIGH MY FRIEND")
print("SORRY YOU LOSE")
    