# Experiment - 10 : Object Oriented Programming - Inheritance
# ============================================================


# Q1. WAP to demonstrate Single Inheritance where a child class
#     inherits a method from a parent class

class Animal:
    def speak(self):
        print("This animal makes a sound")

class Dog(Animal):
    def bark(self):
        print("The dog barks")

my_dog = Dog()
my_dog.speak()
my_dog.bark()

# Output:
# This animal makes a sound
# The dog barks


# -------------------------------------------------------

# Q2. WAP to demonstrate Multilevel Inheritance
#     classes Grandparent with methods property, parent (business()), child, education()

class Grandparent:
    def property(self):
        print("Grandparent own land and house")

class Parent(Grandparent):
    def business(self):
        print("Parent runs a successful family business")

class Child(Parent):
    def education(self):
        print("Child is pursuing higher education")

obj = Child()
obj.property()
obj.business()
obj.education()

# Output:
# Grandparent own land and house
# Parent runs a successful family business
# Child is pursuing higher education


# -------------------------------------------------------

# Q3. WAP to demonstrate Multiple Inheritance
#     classes Father skill1(), Mother skill2(), child skill3()

class Father:
    def skill1(self):
        print("Father is good at gardening")

class Mother:
    def skill2(self):
        print("Mother is good at cooking")

class Child(Father, Mother):
    def skill3(self):
        print("Child is good at painting")

obj = Child()
obj.skill1()
obj.skill2()
obj.skill3()

# Output:
# Father is good at gardening
# Mother is good at cooking
# Child is good at painting
