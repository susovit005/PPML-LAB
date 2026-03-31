# Experiment - 4 : Loops & Number Theory
# ============================================================


# Q1. WAP that prints decimal equivalent 1/2, 1/3, ... 1/100

n = 100
i = 2
while i <= n:
    print(f"1/{i} = {1/i}")
    i += 1

# Output:
# 1/2 = 0.5
# 1/3 = 0.3333333333333333
# 1/4 = 0.25
# ... (continues till 1/100)


# -------------------------------------------------------

# Q2. WAP to test a number prime or not

n    = 5
i    = 2
flag = 0
while i < n // 2:
    if n % i == 0:
        flag = 1
        break
    i += 1
if n > 1 and flag == 0:
    print("Prime Number")
else:
    print("Not a prime Number")

# Output:
# Prime Number


# -------------------------------------------------------

# Q3. WAP to find GCD of 3 numbers. Import math

import math
a          = int(input("Enter first number: "))
b          = int(input("Enter second number: "))
c          = int(input("Enter third number: "))
gcd_result = math.gcd(a, math.gcd(b, c))
print("GCD of three numbers is:", gcd_result)

# Output:
# Enter first number: 12
# Enter second number: 18
# Enter third number: 24
# GCD of three numbers is: 6


# -------------------------------------------------------

# Q4. WAP to find sum of digits of a positive integer

num        = 25
sum_digits = 0
while num > 0:
    sum_digits += num % 10
    num        //= 10
print("Sum of digits", sum_digits)

# Output:
# Sum of digits 7


# -------------------------------------------------------

# Q5. WAP to test a number is palindrome or not

num  = 121
temp = num
rev  = 0
while temp > 0:
    rev  = rev * 10 + temp % 10
    temp //= 10
if num == rev:
    print("Palindrome")
else:
    print("Not Palindrome")

# Output:
# Palindrome


# -------------------------------------------------------

# Q7. Write Fibonacci series up to n terms

n    = int(input("Enter number of terms: "))
a, b = 0, 1
i    = 0
while i < n:
    print(a, end=" ")
    a, b = b, a + b
    i += 1

# Output:
# Enter number of terms: 7
# 0 1 1 2 3 5 8


# -------------------------------------------------------

# Q8. Reverse a number using while loop

num     = 6969
reverse = 0
while num > 0:
    reverse = reverse * 10 + num % 10
    num     //= 10
print("Reversed number", reverse)

# Output:
# Reversed number 9696
