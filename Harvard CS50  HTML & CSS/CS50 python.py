# BASIC PRINT

print ("Hello World");
print ("My name is Phensic")
Name = input("Name: ")
print(f"Hello, {Name}")

# CONDITIONS

num = int(input('Number: '))
if num > 0:
    print("This is a positive number")
else:
    print("Number is not positive")


    

pref = int(input('Number: '))
if pref > 11:
    print('This number is greater than 11')
elif pref < 11 :
    print('This number is less than 11')
else: 
    print('The number is 11 ')
    
#  SEQUENCE
# LISTS => A SEQUENCE OF MUTABLE VALUES 
name = "Mayor"
print(name[1])



# TUPLE =>  SEQUENCE OF IMMUTABLE VALUES
coordinate = (10.0, 20.0)

Name = ["Mayor", "Henry", "Ron", " Hermoine", "Joycee",]
Name.append("Draco")
print(Name[0])
Name.sort()
print(Name)



# SET => A COLLECTION OF UNIWUE VALUES

s = set()

s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(2) # ONLY RETURNS UNIQUE VALUES 

s.remove(3)
print(s)
print(f"The set has {len(s)} elements.")

# DICTIONARY => A COLLECTION OF KEY-VALUE PAIR

houses ={"Harry": "Gryffindor", "Draco": "Slytherin"}
houses["Hermoine"] = "Gryffindor"
print(houses["Hermoine"])




# LOOPS
for i in [0, 1, 2, 3, 4, 5]:
    print(i)

for i in range(20):
    print(i)

Names = ["Rayn", "Raynold", "Blue Shirt Guy", "Tom", "Welling"]

for inputs in Names:
    print(inputs)

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

# # CLASS
# class Point():
#     def __init__(self, x, y)

    


