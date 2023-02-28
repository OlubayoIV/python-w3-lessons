import new

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
    #string length
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

    #boolean operators
name = 'John'
age = 23
if name == 'John' and age == 23:
    print('Ton nom est John, est tu as vingt trois ans aussi.')

if name == 'John' or name == 'Doe':
    print('Your name is either John or Rick.')

if name in ['John', 'Doe']:
    print('Your name is either John or Rick.')

    #if, elif, else statements
x = 2
if x == 2:
    print('x equals two!')
else:
    print('x does nor equal to two.')

    #loops (for)
for x in range(5):
    print(x)        #print out 0, 1, 2, 3, 
    4
for x in range(3, 6):
    print(x)        #print out 3, 4, 5
for x in range(3, 8, 2):
    print(x)        #print out 3, 5, 7 
    #loops (while)
count = 0
while count < 5:
    print(count)
    count += 1
    
    #break
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

for x in range(10):
    if x % 2 == 0:
        continue
    print(x)

    #functions
def my_function():
    print('Hello from my function')
def my_function_with_args(username, greeting):
    print('Hello, %s , From my Function!, I wish you %s' %(username, greeting))
def sum_two_numbers(a, b):
    return a + b

    #try and except
astr = 'hello bob'
try:
    istr = int(astr)
except: 
    istr = -1
    
    print('Backup', istr)
    #class and objects
class MyClass:
    variable = 'blah'

    def function(self):
        print('This is a message inside the class.')

newobject = MyClass()

print(newobject.variable)
newobject.function()
    
    #init function
class NumberHolder:
    def __init__(self, number):
        self.number = number
    def returnNumber(self):
        return self.number
var = NumberHolder(7)
print(var.returnNumber())

    #dictionary
phonebook = {}
phonebook['John'] = 938477566
phonebook['Jack'] = 938377264
phonebook['Jill'] = 947662781

print(phonebook)

del phonebook['Jill']
phonebook['Jake'] = 938273443

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

    #how to find files in python
name = input('Enter file name:')
handle = open(name)

counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1

bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)

    #instagram in python
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    if name not in counts:
        counts[name] = 1
    else :
        counts[name] = counts[name] + 1
print(counts)