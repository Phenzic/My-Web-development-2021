# BASIC PRINT

print ("Hello World")
print ("My name is Phensic")
Name = input("Name: ")
print(f"Hello, {Name}")

# CONDITIONS

num = int(input('Number: '))
if num > 0:
    print("This is a positive number")
else:
    print("Number is Negative")


    

pref = int(input('Number: '))
if pref > 11:
    print('This number is greater than 11')
elif pref < 11 :
    print('This number is less than 11')
else: 
    print('The number is 11 ')
    
# SEQUENCES


# A LISTS => SEQUENCE OF MUTABLE VALUES
name =['Mayor', 'Henry','Ron', 'Hermione', 'Ginny' ] 

name.append('Draco')
name.sort()

print (name)
print(name[1])

# A TUPPLE => SEQUENCE IMMUTABLE LIST
coordinate = (10.0, 20.0)


# A SET => A COLLECTION OF UNIQUE VALUES

s = set()

s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(3)      #NO ELEMENT APPERS TWICE IN THE SET
              # ONLY RETURNS UNIQUE VALUES 

s.remove(2)
print(s)

print (f"This set has {len(s)} elements ")

# A DICTIONARY => A COLLECTION OF KEY-VALUE PAIR (MUTABLE)
houses = {"Harry": "Griffindor", "Draco": "Slytherin" }

print(houses["Harry"])

houses["Hermoine"]= "Gryffindor"

print(houses["Hermoine"])




# LOOPS 
for i in [0, 1, 2, 3, 4, 5]:
    print(i)

for i in range(10):
    print(i)

Names = ["Rayn", "Raynold", "Blue Shirt Guy", "Tom", "Welling"] 
for name in Names:
    print (name)

person = "Salvatore"
for chars in person:

    print(chars)


# FUNCTIONS

def Square(x):
    return(x * x)

for i in range(10):
    print(f"The square of {i} is {Square(i)}")

# ON ANOTHER FILE YOU CAN IMPORT FUNCTIONS BY USING THE INBUILT FUNCTION:
# FROM <FILE NAME> IMPORT SQUARE




# PYTHON OBJECT-ORIENTED PROGRAMMING 

# CLASS
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(2, 8)

print(p.x)
print(p.y)
    

class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passangers = []

    def add_passangers(self, name):
        if not self.open_seats():
            return False    
        self.passangers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passangers) 

flight = Flight(3)

people = ["Harry", "Ron", "Hermoine", "Ginny"]
for persons in people:
    if flight.add_passangers(persons):
        print(f"Added {persons} to the flight succcessfully")
    else:
        print(f"There are no available seats for {persons}")




# DECORATOR => ARE MODIFYERS OF FUNCTIONS
# ( TAKE A FUNCTION WRAPS IT UP AND PRINT OUT A MODIFIED VERSION OF IT)


def announce(f):
    def wrapper():
        print("About to run a function...")
        f()
        print("Done with the function.")
    return wrapper



@announce         #ADDING THE ANNOUNCE DECORATOR
def hello():
    print("Hello, World!")

hello()






# LAMBDA 

Groups = [
    {"Name": "Harry", "House": "Gryffindor"},
    {"Name": "Cho", "House": "Ravenclaw"},
    {"Name": "Draco", "House": "Slytherin"}
]

# def f(person):
#     return person["House"]
# Groups.sort(key = f)
#       OR

Groups.sort(key = lambda person: person["Name"])

print(Groups)


# EXCEPTIONS
import sys

try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Error: Invalid input.")
    sys.exit(1)



try:
    result = x / y
except ZeroDivisionError:
    print("Error: Cannot divide by 0. ")
    sys.exit(1)

print (f"{x} / {y} = {result}")
