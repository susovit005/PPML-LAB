# Experiment - 3 : Conditionals & Decision Making
# ============================================================


# Q1. WAP to test a string is palindrome or not

s   = input("Enter a string: ")
rev = s[:: -1]
if s == rev:
    print("The string is palindrome")
else:
    print("The string is not palindrome")

# Output:
# Enter a string: madam
# The string is palindrome
#
# Enter a string: hello
# The string is not palindrome


# -------------------------------------------------------

# Q2. WAP to input 3 coefficient values and find real roots. Import math

import math
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))
d = b * b - 4 * a * c
if d > 0:
    root1 = (-b + math.sqrt(d)) / (2 * a)
    root2 = (-b - math.sqrt(d)) / (2 * a)
    print("Two real and distinct roots:")
    print("Root 1 =", root1)
    print("Root 2 =", root2)
elif d == 0:
    root = -b / (2 * a)
    print("One real and equal root:")
    print("Root =", root)
else:
    print("No real roots")

# Output:
# Enter coefficient a: 1
# Enter coefficient b: -5
# Enter coefficient c: 6
# Two real and distinct roots:
# Root 1 = 3.0
# Root 2 = 2.0


# -------------------------------------------------------

# Q3. Find the greatest among 3 unequal numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a > b and a > c:
    print("Greatest number is:", a)
elif b > a and b > c:
    print("Greatest number is:", b)
else:
    print("Greatest number is:", c)

# Output:
# Enter first number: 12
# Enter second number: 45
# Enter third number: 30
# Greatest number is: 45


# -------------------------------------------------------

# Q4. Accept a digit within 0 to 6 and display the week day

d = int(input("Enter a digit (0 to 6): "))
if   d == 0: print("Sunday")
elif d == 1: print("Monday")
elif d == 2: print("Tuesday")
elif d == 3: print("Wednesday")
elif d == 4: print("Thursday")
elif d == 5: print("Friday")
elif d == 6: print("Saturday")
else:        print("Invalid input!")

# Output:
# Enter a digit (0 to 6): 3
# Wednesday


# -------------------------------------------------------

# Q5. WAP to input data for int, string, float, Boolean, complex & display their datatypes

a = 10
b = "Hi"
c = 10.5
d = True
e = 3 + 4j
print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))
print(e, type(e))

# Output:
# 10 <class 'int'>
# Hi <class 'str'>
# 10.5 <class 'float'>
# True <class 'bool'>
# (3+4j) <class 'complex'>


# -------------------------------------------------------

# Q6. WAP to input string "Good morning friends" and display reverse, split and store as list

sentence = input("Good morning friends, how are you all: ")
rev      = sentence[:: -1]
print("Reverse", rev)
list     = sentence.split()
print("List of words", list)

# Output:
# Good morning friends, how are you all: Good morning friends, how are you all
# Reverse lla uoy era woh ,sdneirf gninrom dooG
# List of words ['Good', 'morning', 'friends,', 'how', 'are', 'you', 'all']


# -------------------------------------------------------

# Q7. WAP to input string "hi ram hi sam hi niam". Search "hi" replace with "Hello". Remove spaces

text          = "hi ram hi sam hi niam"
replaced_text = text.replace("hi", "Hello")
final_text    = replaced_text.strip()
print("Final result", final_text)

# Output:
# Final result Hello ram Hello sam Hello niam
