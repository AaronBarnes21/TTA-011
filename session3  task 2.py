
print ("enter marks obtained in 4 subjects")
markOne = int(input())
markTwo = int(input())
markThree = int(input())
markFour = int(input())
markFive = int(input())


tot = markOne + markTwo + markThree + markFour +markFive
avg = 5

if avg >= 90 and avg <= 100:
  print("your grade is   A+")
elif avg >= 85 and avg <= 90:
    print("your grade is A")
elif avg >= 72 and avg <= 95:
    print(" your grade is B")
elif avg >= 68 and avg <= 72:
    print("your grade is C")
elif avg >= 52 and avg <= 68:
    print("your grade is D")
else:
    print("invalid input")