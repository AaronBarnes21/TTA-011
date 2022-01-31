import random
myName = input("hello! What is your name?")
number = random.randint(1,10)
print("well,"     +myName+ "i am thinking of a number between 1 and 10")
guess = int(input("Take a guess"))

if guess == number:
     print("Good job" + myName+"! You guessed my number")
else:
     print("Wrong, better luck next time")
    
    
    