# PythonLearn
Python Learn
#there are 15 questions to master in if-elif-else

#Q1. Check if Number is Positive, Negative, or Zero

num = float(input("Enter a number: "))

if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
    
#Q2. Check Voting Eligibility

age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

#Q3. Check if Number is Even or Odd

num = int(input("Enter a number: "))

if num % 2 == 0:
    print(f"{num} Even number.")
else:
    print(f"{num} Odd number.")

#Q4. Find the Largest of Three Numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print(f"{a} islargest number")
elif b >= a and b >= c:
    print(f"{b} is largest number")
else:
    print(f"{c} is largest number")

#Q5. Grade Based on Marks

Maths = int(input("Enter Maths marks: "))
English = int(input("Enter English marks: "))
science = int(input("Enter science marks: ")) 
Average = (Maths + English + science)/3
print(Maths)
print(English)
print(science)
print(Average)
if(Average >= 90 and Average <= 100):
    print("A Grade")
elif(Average >= 80 and Average <90):
    print("B Grade")
elif(Average >= 70 and Average <80):
    print("C Grade")
elif(Average >=60 and Average <70):
    print("D Grade")
else:
    print("Fail")   

#Q5. Grade Based on Marks

marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")
else:
    print("Grade: Fail")

#Q6. Check Leap Year

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("It's a leap year.")
else:
    print("Not a leap year.")

#Q7. Simple Calculator (Add, Subtract, Multiply, Divide)

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

if operation == '+':
    print("Result:", num1 + num2)
elif operation == '-':
    print("Result:", num1 - num2)
elif operation == '*':
    print("Result:", num1 * num2)
elif operation == '/':
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Cannot divide by zero.")
else:
    print("Invalid operation.")

#Q8. Check if Character is Vowel or Consonant

ch = input("Enter a single alphabet: ").lower()

if ch in 'aeiou':
    print("It is a vowel.")
elif ch.isalpha():
    print("It is a consonant.")
else:
    print("Not an alphabet.")

#Q9. Check Password

carrect = input("Enter login password: ")
password = input("Enter password: ")

if password == carrect:
    print("log in")
else:
    print("incarrect password")


#Q10. Print Day Name Based on Number

day = int(input("Enter a number (1 to 7): "))

if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
else:
    print("Invalid input. Please enter a number between 1 and 7.")

#Q11. Check if a number is divisible by both 3 and 5

num = int(input("Enter a number: "))

if num % 3 == 0 and num % 5 == 0:
    print("Divisible by both 3 and 5.")
elif num % 3 == 0:
    print("Divisible by 3 only.")
elif num % 5 == 0:
    print("Divisible by 5 only.")
else:
    print("Not divisible by 3 or 5.")

#Q12. Character Type Checker

ch = input("Enter a character: ")

if ch.isupper():
    print("Uppercase letter.")
elif ch.islower():
    print("Lowercase letter.")
elif ch.isdigit():
    print("Digit.")
else:
    print("Special character.")

#Q13. Assign Job Role Based on Qualification

qualification = input("Enter your qualification: ").lower()

if qualification == "10th":
    print("Not eligible.")
elif qualification == "12th":
    print("Eligible for Internship.")
elif qualification == "graduate":
    print("Eligible for Job.")
elif qualification == "postgraduate":
    print("Eligible for Senior Job.")
else:
    print("Invalid Qualification.")

#Q14. ATM Cash Withdrawal Simulation

balance = 100000
withdraw = int(input("Enter amount to withdraw: "))

if withdraw <= 0:
    print("Invalid amount.")
elif withdraw % 100 != 0:
    print("Enter amount in multiples of 100.")
elif withdraw > balance:
    print("Insufficient balance.")
else:
    balance -= withdraw
    print("Please collect your cash.")
    print(f"Remaining balance : {balance}")
    
#Q15. Rock, Paper, Scissors Game (2 Players)

print("Choices: rock, paper, scissors")
p1 = input("Player 1: ").lower()
p2 = input("Player 2: ").lower()

if p1 == p2:
    print("It's a tie!")
elif (p1 == "rock" and p2 == "scissors") or \
     (p1 == "paper" and p2 == "rock") or \
     (p1 == "scissors" and p2 == "paper"):
    print("Player 1 wins!")
elif (p2 == "rock" and p1 == "scissors") or \
     (p2 == "paper" and p1 == "rock") or \
     (p2 == "scissors" and p1 == "paper"):
    print("Player 2 wins!")
else:
    print("Invalid input!")
