# Experiment - 5 : Fibonacci & For Loop Iteration
# ============================================================


# Q1. Generate Fibonacci series below 0 to 1000, find sum of even valued terms

fibonacci = []
a, b      = 0, 1
while a <= 1000:
    fibonacci.append(a)
    a, b = b, a + b
even_sum = sum(num for num in fibonacci if num % 2 == 0)
print("Fibonacci series upto 1000:")
print(even_sum)

# Output:
# Fibonacci series upto 1000:
# 798


# -------------------------------------------------------

# Q2. WAP to loops over a sequence of elements of list, tuple, dictionary and set

list = [1, 2, 3]
for i in list:
    print(i)

tpl = (4, 5, 6)
for i in tpl:
    print(i)

dict = {"a": 1, "b": 2}
for key, value in dict.items():
    print(key, value)

# Output:
# 1
# 2
# 3
# 4
# 5
# 6
# a 1
# b 2


# -------------------------------------------------------

# Q3. WAP to find the Fahrenheit for given Celsius from list

celsius_list    = [0, 20, 37, 100]
fahrenheit_list = []
for c in celsius_list:
    f = (c * 9 / 5) + 32
    fahrenheit_list.append(f)
print("Celsius    :", celsius_list)
print("Fahrenheit :", fahrenheit_list)

# Output:
# Celsius    : [0, 20, 37, 100]
# Fahrenheit : [32.0, 68.0, 98.6, 212.0]


# -------------------------------------------------------

# Q4. WAP to create an empty list, input numbers, remove duplicates, sort ascending

numbers = []
n       = int(input("How many numbers do you want to enter: "))
for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)
numbers = list(set(numbers))
numbers.sort()
print("Sort list without duplicates:", numbers)

# Output:
# How many numbers do you want to enter: 5
# Enter number 1: 3
# Enter number 2: 1
# Enter number 3: 3
# Enter number 4: 2
# Enter number 5: 1
# Sort list without duplicates: [1, 2, 3]
