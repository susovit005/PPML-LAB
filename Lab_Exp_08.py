# Experiment - 8 : Functions
# ============================================================


# Q1. WAP to find the square of a number

def square(n):
    return n * n
num = int(input("Enter a number: "))
print("Square:", square(num))

# Output:
# Enter a number: 5
# Square: 25


# -------------------------------------------------------

# Q2. WAP to check whether a number is even or odd

def square(n):
    return n * n
num = int(input("Enter a number: "))
print(check(num))

# Output:
# Enter a number: 4
# 16


# -------------------------------------------------------

# Q3. WAP to find the sum of two numbers

def Sum(a, b):
    return a + b
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
print(Sum(a, b))

# Output:
# Enter a number: 5
# Enter a number: 3
# 8


# -------------------------------------------------------

# Q4. WAP to find the factorial of a number

def factorial(n):
    fact = 1
    while n != 1:
        fact *= n
        n    -= 1
    return fact

# Output (n=5):
# 120


# -------------------------------------------------------

# Q5. WAP to check whether a number is prime

def prime(n):
    count = 1
    for j in range(2, n):
        if n % j == 0:
            count += 1
    if count != 1:
        return "Not prime"
    else:
        return "prime"
n = int(input("Enter a number: "))
print(prime(n))

# Output:
# Enter a number: 7
# prime


# -------------------------------------------------------

# Q6. WAP to reverse a string

def reverse(s):
    return s[:: -1]
s = input("Enter a word: ")
print("Reverse word:", reverse(s))

# Output:
# Enter a word: Python
# Reverse word: nohtyP


# -------------------------------------------------------

# Q7. WAP to find largest of three numbers

def largest(x, y, z):
    return max(x, y, z)
print("Largest Number:", largest(5, 6, 3))

# Output:
# Largest Number: 6


# -------------------------------------------------------

# Q8. WAP to count vowels in a string

def count_vowels(s):
    count = 0
    for ch in s:
        if ch.lower() in 'aeiou':
            count += 1
    return count
text = input("Enter a string: ")
print("Vowel Count:", count_vowels(text))

# Output:
# Enter a string: Amandeep
# Vowel Count: 4


# -------------------------------------------------------

# Q9. WAP to calculate SI

def SI(p, r, t):
    return (p * r * t) / 100
p = 1000
r = 2.5
t = 2.5
print("SI:", SI(p, r, t))

# Output:
# SI: 62.5


# -------------------------------------------------------

# Q10. WAP that accepts a list and return the sum of its elements

def sum_list(lst):
    total = 0
    for x in lst:
        total += x
    return total
print(sum_list([1, 2, 3, 4]))

# Output:
# 10
