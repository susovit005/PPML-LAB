# Experiment - 9 : Function Arguments
#                  (Positional, Keyword, Default, *args, **kwargs)
# ============================================================


# Q1. What are positional arguments?
# Positional arguments are passed to a function in the same order
# as parameters defined in function.

def add(a, b):
    return a + b
add(5, 10)

# Output:
# 15


# -------------------------------------------------------

# Q2. WAP using positional arguments

def product(a, b):
    print("product = ", a * b)
product(4, 6)

# Output:
# product =  24


# -------------------------------------------------------

# Q3. What are keyword arguments?
# Keyword arguments are passed using parameter names. Order does not matter.

def display(name, age):
    print(name, age)
display(age=20, name="Ravi")

# Output:
# Ravi 20


# -------------------------------------------------------

# Q4. WAP using keyword arguments

def student(name, course):
    print("Name:", name)
    print("Course:", course)
student(course="python", name="Anu")

# Output:
# Name: Anu
# Course: python


# -------------------------------------------------------

# Q5. What are default arguments?
# Default arguments have predefined values. If no value is passed
# the default value is used.

def greet(name="student"):
    print("Hello", name)
greet()

# Output:
# Hello student


# -------------------------------------------------------

# Q6. WAP using default arguments

def bill(amount=100):
    print("Bill Amount:", amount)
bill(500)
bill()

# Output:
# Bill Amount: 500
# Bill Amount: 100


# -------------------------------------------------------

# Q7. What are arbitrary arguments?
# Arbitrary arguments are used when no. of arguments is not fixed.
# They use *args and **kwargs.

# Q8. WAP using *args

def total(*nums):
    print("Sum =", sum(nums))
total(10, 20, 30)

# Output:
# Sum = 60


# -------------------------------------------------------

# Q9. WAP using **kwargs

def employee(**details):
    for k, v in details.items():
        print(k, ":", v)
employee(name="kiran", id=101, dept="IT")

# Output:
# name : kiran
# id : 101
# dept : IT
