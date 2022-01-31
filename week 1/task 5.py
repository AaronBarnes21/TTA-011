from ast import operator
from pickle import TRUE
from secrets import choice
from tkinter import Y
from traceback import print_tb


def add (x,y):
  return x + y

def subtract (x,y):
    return x - y

def multiply (x,y):
    return x * Y

def divide (x,y):
    return x / y

#select any operator 
 
print("Select operation")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
  choice=input("enter operatror(1/2/3/4): ")

  if choice in('1','2','3','4'):
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter the second number: "))        
    
  if choice == '1':
    print(num1, "+", num2, "=", add(num1, num2))         
    
  elif choice =='2':
    print(num1, "-", num2, "=", subtract(num1, num2))
    
  elif choice == '3':
    print(num1, "*", num2, "=",multiply(num1, num2))
    
  elif choice == '4':
    print(num1, "/", num2, "=", divide(num1, num2))
    
  next_calculation = input("let's do next calculator(yes/no): ")
  if next_calculation == "no":
   break

else:
    print("Invalid Input")