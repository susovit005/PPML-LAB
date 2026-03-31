# Experiment - 6 : For / While with Lists & Dictionaries
# ============================================================


# Q1. WAP to create a list of fruits. Display from last index, show length of each element

fruits   = ["apple", "banana", "Mango"]
print("Elements from last index to first with length:")
i        = len(fruits) - 1
rev_list = []
while i >= 0:
    print(fruits[i], "length", len(fruits[i]))
    rev_list.append(fruits[i][:: -1])
    i -= 1
print("List containing reverse of each element")
print(rev_list)

# Output:
# Elements from last index to first with length:
# Mango length 5
# banana length 6
# apple length 5
# List containing reverse of each element
# ['ognaM', 'ananab', 'elppa']


# -------------------------------------------------------

# Q2. WAP to create a dictionary, input keys and values.
#     Then create another dictionary which collects value of 1st as keys of 2nd

d1 = {}
n  = int(input("Enter no of elements: "))
for i in range(n):
    key   = input("Enter Key: ")
    value = input("Enter value: ")
    d1[key] = value
d2 = {}
for k, v in d1.items():
    d2[v] = k
print("First dictionary")
print(d1)
print("Second dictionary")
print(d2)

# Output:
# Enter no of elements: 2
# Enter Key: a
# Enter value: 1
# Enter Key: b
# Enter value: 2
# First dictionary  {'a': '1', 'b': '2'}
# Second dictionary {'1': 'a', '2': 'b'}


# -------------------------------------------------------

# Q3. WAP to input a sentence, store each word in LIST1, display with index.
#     Create LIST2 as series of numbers. Use zip() to combine both lists

sentence = input("Enter a sentence: ")
list1    = sentence.split()
print("List 1 elements with index")
for index, word in enumerate(list1):
    print(index, ":", word)
list2    = []
i        = 1
while i <= len(list1):
    list2.append(i)
    i += 1
print("List 2 (number series)")
print(list2)
list3    = []
for x, y in zip(list1, list2):
    list3.append((x, y))
print("List 3 (Combined list)")
print(list3)

# Output:
# Enter a sentence: Hello World Python
# List 1 elements with index
# 0 : Hello
# 1 : World
# 2 : Python
# List 2 (number series)
# [1, 2, 3]
# List 3 (Combined list)
# [('Hello', 1), ('World', 2), ('Python', 3)]
