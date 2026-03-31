# Experiment - 7 : Lists, Ranges, Primes & String Analysis
# ============================================================


# Q1. WAP to create a list containing natural numbers from m to n (use for loop).
#     Find sum, avg, largest, smallest in the list

m       = int(input("Enter starting value (m): "))
n       = int(input("Enter ending value (n): "))
numbers = []
for i in range(m, n + 1):
    numbers.append(i)
print("List:", numbers)
total    = sum(numbers)
avg      = total / len(numbers)
largest  = max(numbers)
smallest = min(numbers)
print("Sum =", total, " Avg =", avg, " Largest =", largest, " Smallest =", smallest)

# Output:
# Enter starting value (m): 1
# Enter ending value (n): 5
# List: [1, 2, 3, 4, 5]
# Sum = 15  Avg = 3.0  Largest = 5  Smallest = 1


# -------------------------------------------------------

# Q2. WAP to generate all prime numbers within a given range from m to n

m = 5
n = 10
for i in range(m, n + 1):
    count = 1
    for j in range(2, i):
        if i % j == 0:
            count += 1
    if count == 1:
        print("Prime number:", i)

# Output:
# Prime number: 5
# Prime number: 7


# -------------------------------------------------------

# Q3. WAP to create a string which contains a paragraph. Find:
#     (i) Count how many words it contains
#     (ii) How many palindrome or not
#     (iii) Print each word in reverse order

paragraph            = "Madam from teaches malayalam and level tivic students"
words                = paragraph.split()
total_words          = len(words)
palindrome_count     = 0
non_palindrome_count = 0
for word in words:
    w = word.lower()
    if w == w[:: -1]:
        palindrome_count     += 1
    else:
        non_palindrome_count += 1
print("Reverse words:")
for word in words:
    print(word[:: -1])
print("Total no of words:", total_words)
print("Number of palindrome words:", palindrome_count)
print("Number of non-palindrome words:", non_palindrome_count)

# Output:
# Reverse words:
# madaM
# morf
# sehcaet
# malayalam
# dna
# level
# civit
# stneduts
# Total no of words: 8
# Number of palindrome words: 2
# Number of non-palindrome words: 6
