
# Experiment - 1 : Basic Input / Output & Arithmetic


# Q1. Write a program to print "Welcome to Python World"

print("Welcome to Python world")

# Output:
# Welcome to Python world


# -------------------------------------------------------

# Q2. Write a program to input name, age and address and print them

name    = input("Enter your name: ")
age     = input("Enter your age: ")
address = input("Enter your address: ")
print("\n-- Details --")
print("Name    : ", name)
print("Age     : ", age)
print("Address : ", address)

# Output:
# Enter your name: Amandeep
# Enter your age: 20
# Enter your address: Gunupur
#
# -- Details --
# Name    :  Amandeep
# Age     :  20
# Address :  Gunupur


# -------------------------------------------------------

# Q3. Write a program to find area and perimeter of a circle

pi        = 3.14
r         = float(input("Enter radius of circle: "))
area      = pi * r * r
perimeter = 2 * pi * r
print("Area      :", area)
print("Perimeter :", perimeter)

# Output:
# Enter radius of circle: 5
# Area      : 78.5
# Perimeter : 31.400000000000002


# -------------------------------------------------------

# Q4. Write a program to input two integers, find sum and product of them

a       = int(input("Enter first integer: "))
b       = int(input("Enter second integer: "))
sum     = a + b
product = a * b
print("Sum     : ", sum)
print("Product : ", product)

# Output:
# Enter first integer: 6
# Enter second integer: 4
# Sum     :  10
# Product :  24


# -------------------------------------------------------

# Q5. Write a program to input two numbers, swap using third variable

x    = input("Enter first value: ")
y    = input("Enter second value: ")
temp = x
x    = y
y    = temp
print("After Swap")
print("x = ", x)
print("y = ", y)

# Output:
# Enter first value: 10
# Enter second value: 20
# After Swap
# x =  20
# y =  10


# -------------------------------------------------------

# Q6. Write a program to input two numbers, swap without using 3rd variable

x = input("Enter first number")
y = input("Enter second number")
x = x + y
y = x - y
x = x - y
print("After Swap")
print("x = ", x)
print("y = ", y)

# Output:
# Enter first number5
# Enter second number10
# After Swap
# x =  10
# y =  5


# -------------------------------------------------------

# Q7. WAP to input your marks for three subjects then sum and percentage

m1         = float(input("Marks in subject 1: "))
m2         = float(input("Marks in subject 2: "))
m3         = float(input("Marks in subject 3: "))
total      = m1 + m2 + m3
percentage = (total / 300) * 100
print("Total marks :", total)
print("Percentage  :", percentage)

# Output:
# Marks in subject 1: 85
# Marks in subject 2: 90
# Marks in subject 3: 78
# Total marks : 253.0
# Percentage  : 84.33333333333333


# -------------------------------------------------------

# Q8. WAP to find area and perimeter of a triangle

a         = float(input("Side a: "))
b         = float(input("Side b: "))
c         = float(input("Side c: "))
perimeter = a + b + c
s         = perimeter / 2
area      = (s * (s - a) * (s - b) * (s - c)) ** 0.5
print("Perimeter :", perimeter)
print("Area      :", area)

# Output:
# Side a: 3
# Side b: 4
# Side c: 5
# Perimeter : 12.0
# Area      : 6.0
