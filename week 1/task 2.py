import random

myName = input("hello what is you name?")

number = random.randint (1,100)

print("well," + myName+ "what is your favoutie number from 1 to 100")

choose = int(input("chose a number and will grant you a wish"))

if choose== number:
   
    myName=int(input("nice number" +myName+ "welcome to number game"))

    print("your favorite number"+myName+"will grant you great chickens")

else:
    print ( "your have be favourtie number" +myName+" granted you a bowl of scopians")
