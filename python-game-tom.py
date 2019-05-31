print('Hello Python World')
print('Welcome to the number guessing game')
print('Please enter a number from 0 to 1000')
myguess = input()
myintguess = int(myguess)
answer = 146
while myguess != answer:
    print('Incorrect Answer')
    print('Please Try Again')
    newguess = input()
    newguessint = int(newguess)
    if newguessint == answer:
        break

print('Congragulations on Answering Correctly')

print ('You Win a Bag of Dicks')