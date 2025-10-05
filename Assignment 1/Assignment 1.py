#Basic If-Else Problems:

#1 Write a program to check whether a number is positive, negative, or zero.
'''
num = int(input("Enter Number : "))
if num == 0:
    print("Entered Number is 0")
elif num%2 == 0:
    print("Entered Number is Even")
else :
    print("Entered Numver is Odd")
'''

#2 Write a program to check whether a number is even or odd. 
'''
num = int(input("Enter Number : "))
if num%2 == 0:
    print("Entered Number is Even")
else :
    print("Entered Numver is Odd")
'''

#3 Write a program to check if a given year is a leap year or not. 

'''
year = int(input("Enter Year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not Leap Year")
'''

#4 Write a program to find the greatest of two numbers. 
'''
num1 = int(input("Enter First Number : "))
num2 = int(input("Enter Second Number : "))
if (num1 == num2):
    print("The entered numbers are equal")
elif (num1>num2):
    print("The First number is greater")
else :
    print("The second number is greater")
'''

#5 Write a program to check whether a person is eligible to vote (age >= 18).
'''
age = int(input("Enter Age : "))
if age >= 18:
    print("Eligible to Vote")
else :
    print("NOT Eligible to Vote")
'''

#6 Write a program to check whether a given character is a vowel or consonant.
'''
char = input("Enter character : ")
if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
    print("Entered Character is a Vowel")
elif len(char) >=2:
    print("Enter single Character")
else :
    print("Entered Character is a Consonant")
'''

#7 Write a program to check if a number is divisible by 5. 
'''
num = int(input("Enter number : "))
if num % 5 == 0:
    print("Divisible by 5")
else :
    print("Not divisible by 5")
'''

#8 Write a program to determine whether a given number is a single-digit, two-digit, or more than two-digit number.  
'''
num = input("Enter number : ")
length = len(num)
if length == 1 :
    print("Single Digit")
elif length == 2 :
    print("Two Digit")
else :
    print("More than two-digit")
'''

#9 Write a program to check whether a student has passed or failed (passing marks = 40). 
'''
marks = int(input("Enter marks : "))
if marks >= 40 :
    print("Passed")
else :
    print("Failed")
'''

#10 Write a program to find whether the entered number is a multiple of both 3 and 7. 

'''
num = int(input("Enter number : "))
if num % 3 == 0 and num % 7 == 0:
    print("Multiple of both 3 and 7")
else:
    print("Not a multiple of both 3 and 7")
'''


#Ladder If & Nested If:

#1 Write a program to find the greatest among three numbers. 
'''
a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
c = int(input("Enter third number : "))
if a >= b and a >= c:
    print("The greatest number is:", a)
elif b >= a and b >= c:
    print("The greatest number is:", b)
else:
    print("The greatest number is:", c)
'''

#2# Write a program to classify a person based on age: Child (<13), Teenager (13-19), Adult (20-59), Senior (60+).
'''
age = int(input("Enter age : "))
if age < 13:
    print("Child")
elif age >= 13 and age <=19:
    print("Teenager")
elif age >= 20 and age <=59:
    print("Adult")
elif age > 60:
    print("Senior")
else :
    print("60??? No condition when age is 60")
'''

#3 Write a program to assign grades based on marks: 90-100: A,  75-89: B, 50-74: C,  35-49: D, <35: Fail.
'''
marks = int(input("Enter marks : "))
if marks < 35:9
    print("Fail")
elif marks >= 35 and marks <=49:
    print("Grade D")
elif marks >= 50 and marks <=74:
    print("Grade C")
elif marks >= 75 and marks <=89:
    print("Grade B")
elif marks >= 90 and marks <=100:
    print("Grade A")
else :
    print("Enter valid grades")
'''

#4 Write a program to check the type of triangle (equilateral, isosceles, or scalene) based on sides. 
'''
a = int(input("Enter side a: "))
b = int(input("Enter side b: "))
c = int(input("Enter side c: "))
if a + b > c and b + c > a and c + a > b:
    if a == b == c:
        print("Equilateral Triangle")
    elif a == b or b == c or c == a:
        print("Isosceles Triangle")
    else:
        print("Scalene Triangle")
else:
    print("Not a Triangle")
'''

#5 Write a program to check if a character is uppercase, lowercase, digit, or special symbol.
'''
char = input("Enter a character: ")
if len(char)==1 :
    if char.isupper():
        print("The character is an Uppercase letter.")
    elif char.islower():
        print("The character is a Lowercase letter.")
    elif char.isdigit():
        print("The character is a Digit.")
    else:
        print("The character is a Special symbol.")
else :
    print("Enter Single character")
'''

#6 Write a program to calculate electricity bill based on units: Up to 100 units: ₹5 per unit, 101–200 units: ₹7 per unit, Above 200 units: ₹10 per unit.
'''
units = int(input("Enter total unuts: "))
if units <= 100:
    bill = units * 5
elif units >100 and units <= 200:
    bill = 500 + ((units - 100) * 7)
else:
    bill = 500 + 700 + ((units - 200) * 10)
print("Yout bill is : ", bill,"Rupees")
'''

#7Write a program to determine the largest of four numbers using nested if.
'''
a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
c = int(input("Enter third number : "))
d = int(input("Enter Fourth number : "))
largest = 0
if a == b or a == c or a == d or b == c or b == d or c == d :
    print("Enter Distinct numbers ")
elif a > b : 
    if a > c :
        if a > d :
            largest = a
        else :
            largest = d
    else :
        if c > d :
            largest = c
        else :
            largest = d 
        print("The largest number is : ", largest)
else:
    if b > c :
        if b > d :
            largest = b
        else:
            largest = d
    else:
        if c > d :
            largest = c
        else:
            largest = d
        print("The largest number is : ", largest)
'''

#8 Write a program to check if a given year is a century year and also a leap year.
'''
year = int(input("Enter Year: "))
if (year % 400 == 0):
    print("Century Year and also Leap Year")
else:
    print("Not a Century Year and Leap Year")
'''
'''
year = int(input("Enter Year: "))
if year % 100 == 0:  
    if year % 400 == 0:
        print("Century Year and Leap Year")
    else:
        print("Century Year but not a Leap Year")
else:    
    if year % 4 == 0:
        print("Not a Century Year but a Leap Year")
    else:
        print("Neither a Century Year nor a Leap Year")
'''

#9 Write a program to classify BMI value: Underweight (<18.5), Normal (18.5-24.9), Overweight (25-29.9), Obese (30+).
'''
mass = float(input("Enter Weight/Mass : "))
height = float(input("Enter Height in meters : "))
bmi = (mass)/((height)**2)
if bmi < 18.5 :
    print("Underweight")
elif bmi >= 18.5 and bmi <= 24.9 :
    print("Normal")
elif bmi >= 25 and bmi <= 29.9:
    print("Overweight")
else :
    print("OBESE")
print("BMI is : ",bmi)
'''

#10 Write a program to display the smallest number among three using nested if.
'''
a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
c = int(input("Enter third number : "))
low = 0
if a == b or b == c or a == c :
    print("Enter unique numbers")
elif a < b :
    if a < c :
        print(a," is the smallest number")
    else :
        print(c," is the smallest number")
else :
    if b < c :
        print(b," is the smallest number")
    else :
        print(c," is the smallest number")
'''

#For Loop Problems:


#1 Write a program using a for loop to print all Armstrong numbers between 100 and 999. (Armstrong number: sum of cubes of digits equals the number itself. Example: 153 => 1³+5³+3³ = 153).

#i = 100
#while i >= 100 and i <= 999 :
#    string = str(i)
    
#2 Write a program to generate and display the first n prime numbers using a for loop.
'''
n = int(input("Enter number of prime numbers : "))
count = 0
num = 1
while count < n :   
    for i in range(2, num) :
        if num % i == 0 :
            break 
    else :
        print(num , " ")
        count = count+1
    num = num+1
'''

#3  Write a program to display all numbers from 1 to 500 that are divisible by 3, but the sum of their digits should not exceed 10. 
'''
for num in range(1, 501) :
    if num % 3 == 0 : 
        sumd = 00
        for digit in str(num) :
            sumd = sumd + int(digit)
        if sumd <= 10:
            print(num) 
'''

#4 Write a program using a for loop to print a pyramid of stars (*) of height n. Example for n=4: 
r'''
n = int(input("Enter height ofpyramid : "))
for i in range(1, n + 1) :
    stars = 2 * i - 1
    print("*" * stars)
'''

#5 Write a program to accept a string and check whether it is a pangram (contains all 26 alphabets at least once) using a for loop. 
'''
string = input("Enter string : ").lower()
alphabets = "qwertyuiopasdfghjklzxcvbnm"
found = 0

for i in range(0,26) :
    ch = alphabets [i]
    if string.count(ch) > 0 :
        found = found+1
if found == 26 :
    print("Pangram")
else:
    print("Not a Pangram")
'''

#6 Write a program using a for loop to print all twin primes between 1 and 100. (Twin primes: pairs of prime numbers with a difference of 2, e.g., (3,5), (11,13)). 
'''
for num in range(2, 99) :
    for i in range(2, num) : 
        if num % i == 0 :
            break
         
    else :        
        twin = num + 2
        for j in range(2, twin) :
            if twin % j == 0:
                break
        else:
            print(num,twin)
'''

#7 Write a program that accepts a number from the user and prints whether it is a Harshad number (number divisible by the sum of its digits) using a for loop. 
'''
num = int(input("Enter a number : "))
temp = num 
sumd = 0

for digit in str(temp) :
    sumd += int(digit)

if num % sumd == 0 :
    print(num, "Harshad number")
else :
    print(num, "Not Harshad number")
'''
