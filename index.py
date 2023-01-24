print('The following code is PYTHON')

print("Hello Python!")
if 5 > 2:
    print("Five is greater than two!")
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