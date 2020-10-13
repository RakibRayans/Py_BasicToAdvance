#add value in the list
'''
#1
numbers = [5, 6, 7, 8, 9]
numbers.append(20)              #here number add in the end of the list
print (numbers)

#2
numbers = [5, 6, 7, 8, 9]
numbers.insert(1,20)             #here number add at the given index of the list
print (numbers)

#3
numbers = [5, 6, 7, 8, 9]
numbers.remove(8)
print (numbers)

#4
numbers = [5, 6, 7, 8, 9]
numbers.clear()             #here all the number will be gone
print (numbers)

#5
numbers = [5, 6, 7, 8, 9]
numbers.pop()                 #it delete last number
print (numbers)

#6
numbers = [5, 6, 7, 8, 9]
print(numbers.index(7))        #it shows index of the numbers

#7
numbers = [5, 6, 7, 8, 9]
print(6 in numbers)            #number exist or not

#8
numbers = [5, 6, 7, 8, 9,5]
print(numbers.count(5))         #count repeting

#7
numbers = [5, 6, 7, 8, 9]
numbers.sort()
numbers.reverse()
print(numbers)

#8
numbers = [5, 6, 7, 8, 9]
numbers2 = numbers.copy()        #if we change orginal one not gonna happen in th copy list
numbers.remove(8)
print(numbers)
print(numbers2)

#exercise
#remove dublicate values
numbers = [5, 6, 5, 6, 7, 8, 6, 5, 7, 8]
uniques = []
for n in numbers:
    if n not in uniques:
        uniques.append(n)
print(uniques)
'''

#Topples
'''
coordinets = (1, 2, 3)

x,y,z = coordinets           #pythone feature give the similar result of comment code
                             #x = coordinets[0],y = coordinets[1],z = coordinets[2]

print(coordinets[1])
'''

#let's try python dictionary

'''
customer = {
    "name" : "Rakib Rayans",
    "age" : 24,
    "contact_no" : "01644199177",
    "is_verified" : True

}
customer["name"] = "Jon smith"
customer["birthdate"] = "20th January 1996"
print(customer["name"])
print(customer["age"])
print(customer["birthdate"])
print(customer["contact_no"])
print(customer.get("Designation"))
'''

#Exercise (get phone number and convert it to string value
'''
phone = input("Phone: ")
digits_mapping = {
    "0" : "zero",
    "1" : "one",
    "2" : "two",
    "3" : "three",
    "4" : "four",
    "5" : "five",
    "6" : "six",
    "7" : "seven",
    "8" : "eight",
    "9" : "nine"
}

output = ""
for ch in phone:
    output+= digits_mapping.get(ch, "!") + " "
print(output)
'''

#define function
'''
def great_user():
    print("Hi there")
    print("Welcome ur new home.")


print("Start")
great_user()
print("Finish.")
'''
#pass peramiter
'''
def great_user(name):
    print(f"Hi {name}")
    print("Welcome ur new home.")


print("Start")
great_user("Jon")
great_user("merry")
print("Finish.")
'''
#multiple pera miter
'''
def great_user(first_name,last_name):
    print(f"Hi {first_name} {last_name}!")
    print("Welcome ur new home.")


print("Start")
great_user("Jon","smith")

print("Finish.")
'''
#set argument position
'''
def great_user(first_name,last_name):
    print(f"Hi {first_name} {last_name}!")
    print("Welcome ur new home.")


print("Start")
great_user(last_name="Smith",first_name="John")

print("Finish.")
'''

#return funtion
'''
def square(number):
   return number * number


print(square(3))
'''

#error handeling
'''
try:
    age = int(input("age: "))
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print("Age cannot be 0.")
except ValueError:
    print("Invalid value.")
'''

#class in python
'''
class point:
    def move(self):
        print("Move")
    def draw(self):
        print("Draw")


point1 = point()
point1.move()
print(point1)
'''

#constructing object in the class
'''
class Point:
    def __init__(self, x, y):               #here x,y object is construct/creat
        self.x = x
        self.y = y

point = Point(10, 20)
print(point.x)
'''

#exercise
#1
'''
class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print("Talk")


seller = Person("Rakib Rayans")
seller.talk()
print(seller.name)
'''
#2
'''
class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print(f"hi, i am {self.name}")


seller1 = Person("Rakib Rayans :)")
seller1.talk()

seller2 = Person("Anik :)")
seller2.talk()
'''

#inheritance in python
'''
class Animal:
    def __init__(self, name):
        self.name = name
        print(f"Animal name is  {self.name}")
    def type(self):
        print("type")
class Dog(Animal):
    def walk(self):
        print("Walk")
class Cat(Animal):
    pass


dog1 = Dog("Qizaer")
dog1.walk()
dog1.type()
'''

#find the maximum number using function
'''
import utils

numbers = [10, 40, 54, 65, 78]
max = utils.find_max(numbers)

print(max)
'''
#2
'''
from utils import find_max

numbers = [10, 40, 54, 65, 78]
max = find_max(numbers)

print(max) 
'''

#3
from utils import find_max

numbers = [10, 40, 54, 65, 78]
#max = find_max(numbers)

print(max(numbers))



