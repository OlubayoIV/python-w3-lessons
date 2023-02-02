print('The following code is PYTHON')

print("Hello Python my name is Ayo!")
if 5 > 2:
    print("Five is greater than two!")
    #variable and types
    #numbers(integers and floats)
    #integers
myint = 7
print(myint)

    #floats
myfloat = 7.0
print(myfloat)
    #or
myfloat = float(7)
print(myfloat)

    #strings
mystring = "hello my name is Ayo and i'm learning react"
print(mystring)

    #lists
mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist[0])
print(mylist[1])
print(mylist[2])

for x in mylist:
    print(x)

    #arithmetic operators
number = 1 + 2 * 3 / 4.0
print(number)

remainder = 11 % 3
print(remainder)

    #operators with strings
helloworld = "hello" + ' ' + "world"
print(helloworld)

    #operators with lists
even_numbers = [2, 4, 6, 8]
odd_numbers = [1, 3, 5, 7]
all_numbers = odd_numbers + even_numbers
print(all_numbers)

    #string formatting
name = 'John'
age = 23
print('Hello, %s is %d years old.' % (name, age))
    #string lenght
astring = 'Hello world!'
print("single quotes are ' '")
print(len(astring))
    #string index
astring = 'Hello World!'
print(astring.index("o"))
    #string count
astring = 'Hello World!'
print(astring.count("l"))

    #conditions
x = 2
print(x == 2)
print(x == 3)
print(x < 3)
    #global variables
x, y, z = 'Orange', 'Banana', 'Watermelon'
print(x)
print(y)
print(z)
a = b = c = 'Apple'
print(a)
print(b)
print(c)
fruits = ["lemon", "coconut", "grape"]
d, e, f = fruits
print(d)
print(e)
print(f)
g = 'Python '
h = "is "
i = "awesome"
print(g + h + i)

    #keywords without global variable
x = "awesome"

def myfunc():
    print("python is " + x)

myfunc()
print("Python is " + x)

    #global keywords
x = "awesome"
def myfunc():
    global x
    x = "fantastic"
myfunc()
print("Python is " + x)

    #random
import random
print(random.randrange(1, 10))

#positioning in python
j = "Hello Python!"
print(j[1])

#checking lenght
k = 'hello Python!'
print(len(k))

#check string
txt = 'The best things in life are free'
print('free' in txt)

txt = 'The best things in life are free'
if 'free' in txt:
    print('Yes, "free" is present.')

#check string second part
txt = 'The best things in life are free'
print('chere' in txt)

txt = 'The best things in life are free'
if 'chere' not in txt:
    print('No, "chere" is NOT present.')

    #slicing
l = "Hello Python!"
print(l[2:5])

    #while loops
i = 1
while i < 6:
    print(i)
    i += 1

    #break statement
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

    #for loop
portables = ['Samsung', 'Iphone', 'Google-pixel']
for x in portables:
    print(x)

    #range
for x in range(1, 23, 2):
    print(x)     
    '''where it's default starts as o if empty and the 
         third letter indicates how it should incremenet
           because by default it increment by 1'''
    #for loops cannot be empty but if i need an empty one
    #to avoid errors i should put in a 'pass' statement

    #functions in python
def my_function():
    print('new pyhton')
    my_function()