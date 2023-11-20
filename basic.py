name = input("Name:")
print("Hello"+" "+ name)
print("Hello, "+name)
# we can use formatted string like below
print(f"Hello {name}")

# CONDITIONS:
n = int(input("Number: "))
if n>0:
    print("n is positive")
elif n<0:
    print("n is negative")
else:
    print("n is zero")

# SEQUNENCES
name = "Harry"
# THIS [] TAKES SOME ORDERED SEQUENCE OF ELEMENTS & GETS ACCESS TO ONE PARTICULAR ELEMENT INSIDE THAT ONE PARTICULAR SEQUENCE
print(name[2])
 
names = ["Harry", "Ron", "Hermonie"]
print(names[1])

# TUPLES: TWO VALUES TOGETHER '()'

CoordinateX = 10.0
CoordinateY = 20.0

Coordinate =  (10.0,20.0)

# DATA STRUCTURES
# LIST --> Sequence of mutable values
# TUPLE --> Sequence of immutable values
# SET --> Collection of unique values
# DICT --> Collection of key-value pair

# Appending the list
names =  ["Harry", "Ron", "Hermonie"]
names.append("Keyy")
names.sort()
print(names)


# Create an empty set
s = set() 
# Adding element the set
s.add(1)
s.add(2)
s.add(3)
s.add(3)
s.add(4)
# It does'nt allow the element to appear more than once
s.remove(2)
print(s)

print(f"The set has {len(s)} elements.")
# Can include any expression in python that I would lise to substitute into the string

# LOOPS:
for i in range (5):
    print(i)
names = ["fhfh","huigfu","huhvuh"]
for name in names:
    print(name)

name ="Dhathri"
for character in name:
    print(name)
    print(character)

# DICTIONARIES:
houses={"harry":"gfyigf","ronnie":"hfuhuf","harmonie":"kopjpo"}
print(houses["harmonie"])
# TO ADD SOME VALUE TO SOME OTHER VALUE:
houses["harmonie"]="ddijdo"
print(houses["harmonie"])


# FUNCTIONS:
def square (x):
    return x*x
for i in range(10):
    print(f"the square of {i} is {square(i)}")

# IMPORTING THE FUNCTION:
import functions
for i in range(10):
    print(f"the square of {i} is {functions.square(i)} ")

