"""
print("Rakib Rayans")
print("0----")
print(" ||||")
print("*" *  20)
"""
"""
price=100
price = price+23
print(price)
"""
     # some simple things
"""
name = input('What is your name? ')
colour = input('What is favorite colour? ')
print(name+ " likes " + colour)
"""

""""
birth_year = input("Enter your birthyear: ")
#print(type(birth_year))
age= 2020- int(birth_year)
print(age)
#print(type(age))
"""
'''
weight_lbs=input("how  much your weight in pound? ")
weight_kg = .454 * float(weight_lbs)
print(weight_kg)
'''


        ######strinng######

""""
course = 'Python course for "beginners"'
print(course)
"""
'''
course = "Python course for beginners"
print(course)
print(course[0])    #it will show first one,similarly others
print(course[-1])   #it will show last one, similarly -2,-3,-4 so on
print(course[0:3])  #it will show index 0-2 , similarly others
print(course[7:])  #it will show from index 7 to last  , similarly [1:5] ,[3:8] and so on
print(course[:])    #it will show all
'''

'''
name = "Jennifer"
print(name[1:-1])  #what is the out put?
print(len(name))
'''

'''
first = 'Rakib'
last = 'Rayans'
#text= first + ' [' + last + '] ' + 'is a coder'
messege= f'{first} [{last}] is a coder'           #four methode string process (dynamic)
#print(text)
print(messege)
'''

'''
course = 'python for biginners '
print(len(course))
print(course.lower())      #converting all to lower
print(course.upper())      #converting all to upper
print(course.find('o'))     #find the index of the result
print(course.find('O'))     #this methode is case sensetive thats why result is "-1"
print(course.find('biginners'))    #we can search by word/string
print(course.replace("python","Java script"))
print('python' in course)       #it will show bolian result true/flase
'''

#arithmatic operators

'''
print(10 + 3)    #addition
print(10 - 3)    #subtraction
print(10 % 3)    #reminder
print(10 / 3)    #floating result
print(10 // 3)   #int result
print(10 * 3)    #multiplication
print(10 ** 3)   #power 10^3
'''

#assignment operator
'''
x= 10
#x = x + 3
#x+=3        #similarly -,*,/
x= x + 10 + 2 * 3 ** 2    #power,multipli/division,addition,subtraction
print(x)
'''

#function with number

'''
import math

x = 2.6
print(math.ceil(x))
print(math.floor(x))
print(round(x))
print(abs(-2.45))
'''

#condition

'''
is_hot = False
is_cold = False

if is_hot:
    print("It's a hot day")    #if true
    print("Drink planty water")
elif is_cold:
    print("It's a cold day")      #if false
    print("Wear warm clothes")

else:
    print("It's a lovely day")
'''
#exercise

'''
price = input("House price in dollar? ")
p = int(price)

has_good_credit = False

if has_good_credit:
   down_payment = p * 0.1
   total_payment = p - down_payment
else :
    down_payment = p * 0.2
    total_payment = p - down_payment

print(f'The down payment is : {down_payment} $')    #four methode
print(f"You have to pay {total_payment} $")
'''

#logical operator
#if aplicant has high income and good credit ,eligible for loan
'''
has_high_income = True
has_good_credit = True

if has_high_income and has_good_credit :   #similarly "or" operator
    print("Eligible for Loan.")
else:
    print("Not Eligible for loan.")
print("Thank you for ur time :) ")
'''

#if aplicant has high income and good credit ,eligible for loan
'''
has_good_credit = True
has_criminal_record = False

if has_good_credit and not has_criminal_record :   #similarly "or" operator
    print("Eligible for Loan.")
else:
    print("Not Eligible for loan.")
print("Thank you for ur time :) ")
'''

#comperison operator
'''
temperature = input("Enter the temperature : ")
tem = int(temperature)

if tem > 30:
    print("It's a hot day.")
elif tem < 10:
    print("It's a cold day.")
else:
    print("It's a nor hot or cold day.")
'''
#exersise
'''
name = input("Enter your name here : ")
length= len(name)
if length > 10:
    print("Name can't be maximum of 10 characters.")
elif length < 3:
    print("Name must be at least 3 characters.")
else:
    print(f"Yeah we got ur name: {name}")
'''

#weight kg to pound / pound to kg
'''
w = input("Enter weight: ")
weight = int(w)
k = weight * .45        #.454 pound = 1 kg
p = weight / .45
type = input("enter weight type u entered lb(l) or kg(k): ")

if type.upper() == "L":
    print(f"Your weight is {k} kg.")
else:
    print(f"Your weight is {p} pound.")
'''

#while loop
'''
i = 1
while i<=5:
    print("*" * i)
    i = i + 1
print("Done ")
'''

#secret number game
"""
secret_number = 9
i = 0
while i<3:
    n = int(input("Guess:"))
    i = i+1
    if n== secret_number:
        print("You Won!.")
        break
else:
    print("sorry, You loss.")
"""

#engin of a car
'''
command = ""
started = False
while True:
    command = input("> ").lower()

    if command == "help":
        print("""
 start - to start the car
 stop - to stop the car
 quit - to end process       
        """)
    elif command == "start":
        if started:
            print("Car is already started.")

        else:
            started = True
            print("Car is started...")

    elif command == "stop":
        if not started:
            print("Car is already stoped.")

        else:
             started = False
             print("Car is stopped.")

    elif command == "quit":
        print("End process")
        break
    else:
        print("Sorry,I don't understand that...")
'''

#For loop
'''
#1
#item caring index value 

for item in "Python":        #it will print all the characters of the word in new line
    print(item)

#2
for item in ["rakib","roni","anik"]:      #it will print the name in new line
    print(item)

#3
for item in [1,2,3,4,5]:                  #it will print all numbers in new line
    print(item)

#4
for item in range (10):                   #it means upper limit
    print(item)

#5
for item in range (5,10):                 #it mean lower=5 ,upper=10  limit
    print(item)

#6
for item in range(5,10,2):                     #it means  lower=5, upper=10, diff=2
    print(item)

'''

#exercise for loop
'''
prices = [10, 20, 30]

total = 0
for price in prices:             #price carry index value of pricess
    total += price

print(f"Total price= {total}")
'''

#nested loop
#generate cordinate like (1,2) (3,4)
'''
for x in range(4):
    for y in range(3):
        print(f"({x}, {y})")
'''

#exercise (print the star)
'''
numbers = [5, 2, 5, 2, 2]

for x in numbers:
    print("x" * x)
'''

#print from index exercise

#1   print name with given index
'''
n = int(input("Enter index number: "))
name = ['Rakib', 'Akash', 'Anik', 'Raihan', 'Rajib', 'Rito','Sadi']
print(name[n-1])
'''
#2     replace a name
'''
n = int(input("Enter index Which u want to replace: "))
name = ['Rakib', 'Akash', 'Anik', 'Raihan', 'Rajib', 'Rito','Sadi']
name[n-1] = 'Sifat'
print(name)
'''

#3  find the largest number of the list
'''
numbers = [34, 54, 23, 56, 67, 8, 9,78 ,90 , 32, 123]
max = numbers[0]

for number in numbers:
    if number> max:
        max = number
    else:
        continue
print(f"largest number : {max}")
'''

#metrix  two dimentonal loop
'''
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
#print(matrix[1][2])
matrix[2][1] = 15
print(matrix)
'''

#ettarate the matrix

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:
    for itm in row:
        print(itm)

