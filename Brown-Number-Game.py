from random import randint

# variables
upper = 10
lower = 1
guess = 0
x = randint(lower, upper)

# game start
print ("Hello Clarice.  Let's play a game.")

while guess != x:
    print("Pick a number between 1 and 10")
    guess = int(input())
    print("You selected",guess)
    if guess != x:
        print ("Quid pro quo, try again")
    else:
        print ("All good things to those who guess correctly")

print ("I do wish we could play longer, but I'm having an old friend for dinner.")
