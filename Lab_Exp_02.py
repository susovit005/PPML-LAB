# Experiment - 2 : Strings, Lists, Tuples & Dictionaries
# ============================================================


# Q1. Display Simple Interest and Compound Interest

p  = float(input("Principle amount: "))
r  = float(input("Rate of interest: "))
t  = int(input("Time of years: "))
si = (p * r * t) / 100
print("Simple interest is", si)
ci = (p * (1 + r / 100) ** t) - p
print("Compound interest is", ci)

# Output:
# Principle amount: 1000
# Rate of interest: 10
# Time of years: 2
# Simple interest is 200.0
# Compound interest is 210.00000000000023


# -------------------------------------------------------

# Q2. WAP to input 1st name, mid name & last name into 3 variables and apply concatenation

first     = input("Enter first name: ")
middle    = input("Enter middle name: ")
last      = input("Enter last name: ")
full_name = first + " " + middle + " " + last
print("Full name is", full_name)

# Output:
# Enter first name: Amandeep
# Enter middle name: Singh
# Enter last name: Kumar
# Full name is Amandeep Singh Kumar


# -------------------------------------------------------

# Q3. WAP to create a list by initializing with different fruits and display them

fruits = ["Apple", "Mango", "Banana", "Orange", "Grapes"]
print("List of fruits is", fruits)

# Output:
# List of fruits is ['Apple', 'Mango', 'Banana', 'Orange', 'Grapes']


# -------------------------------------------------------

# Q4. WAP to create a tuple and display elements of it

tuple = ("Computer", "Lab", "CSE", "Python")
print("Tuple elements are", tuple)

# Output:
# Tuple elements are ('Computer', 'Lab', 'CSE', 'Python')


# -------------------------------------------------------

# Q5. WAP to create a dictionary, store sample data and display keys, values of it

student = {"Name": "Hara", "Roll no": 230, "Course": "Btech"}
print("Keys",   student.keys())
print("Values", student.values())
print("Full dict", student)

# Output:
# Keys   dict_keys(['Name', 'Roll no', 'Course'])
# Values dict_values(['Hara', 230, 'Btech'])
# Full dict {'Name': 'Hara', 'Roll no': 230, 'Course': 'Btech'}


# -------------------------------------------------------

# Q6. WAP to input a sentence and print reverse of it

sentence     = input("sentence: ")
reverse_text = sentence[:: -1]
print("Reversed sentence", reverse_text)

# Output:
# sentence: Hello World
# Reversed sentence dlroW olleH


# -------------------------------------------------------

# Q7. WAP to input a string "HelloWorld". Display uppercase, lowercase, length and 1st letter upper

text = input("HelloWorld: ")
print(text.upper())
print(text.lower())
print(text.capitalize())
print(len(text))

# Output:
# HelloWorld: helloworld
# HELLOWORLD
# helloworld
# Helloworld
# 10
