# Loops


"""
When we need to do something repeatedly, we are using loops. 
"""

## While Loops

"""
Executes block of code multiple time

SYNTAX:

while <condition>:
     <code>


as long as the condition is true, the code will run

"""

i = 1

while i <= 6:       ### as long as i less or equal than 6, 
    print(i)        ### it will print the value of i
    i = i + 1       ### this will change the value of i in every iteration so it will not run the same code forever. That means the condition will not be always true.


"""RESULT
1
2
3
4
5
6
"""

x = 6

while 0 < x <= 6:       
    print(f"Value of x = {x} -- ", '*' * x)       
    x = x - 1 

"""
Value of x = 6 --  ******
Value of x = 5 --  *****
Value of x = 4 --  ****
Value of x = 3 --  ***
Value of x = 2 --  **
Value of x = 1 --  *
"""

### While Loop with 'else'

"""
else part is executed if the condition in the while loop 
evaluates to False.
"""


counter = 0

while counter < 3:
    print(f"{counter} -- Inside loop")
    counter = counter + 1
else:
    print(f"{counter} -- Inside else")


"""OUTPUT
0 -- Inside loop
1 -- Inside loop
2 -- Inside loop
3 -- Inside else
""" 


### Terminating the Loop

"""
break statement terminates the loop containing it.
"""




fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

j = 0

while j < len(fruits):
    if fruits[j] == 'apple':
        break
    print(fruits[j])    
    j += 1

"""
orange
"""   



#### continue statement


"""
While break statement terminates the whole loop, the continue statement terminates just the iteraton 
and continues the rest of the loop.
"""


j = 0

while j < len(fruits):
    
    
    if fruits[j] == 'apple':
        j += 1
        continue      
    print(fruits[j])
    j += 1

"""
orange
pear
banana
kiwi
banana
"""


### Infinite Loops

"""
while True:
     print('foo')
"""

### Pass Statement

"""
used  to write empty loops.
"""

word = 'Python'
letter = 'o'

while letter not in word:
    pass



### One-Line while Loops


n = 5
while n > 0: n -= 1; print(n)

"""OUTPUT
4
3
2
1
0
"""

## For Loops


"""
used to iterate over items of collection

break, continue, pass can be used to here too
"""

for item in 'Python':
    print(item)

"""
P
y
t
h
o
n
"""

for item in ['orange', 'apple', 'pear']:
    print(item)

"""
orange
apple
pear
"""    

for number in range(3):
    print(number)

"""
0
1
2
"""    


for number in range(6, 12, 2):
    print(number)

"""
6
8
10
"""    

prices = [12, 45, 0, 32, 21, 0, 10]
total = 0

for price in prices:
    if price != 0:
        total += price
    else:
        continue    

print(f"Total cost is {total}") ### 120




keys = []
values = []

someone = {
   "id": "9090",
   "class": 4,
   "isStudent": True
   }

for key, value in someone.items():
    keys.append(key)
    values.append(value)




## Nested Loops

"""
We can use them as nested for ex. while loop in a for loop or for loop in a while loop or while loop in a while loop etc.
"""

numbers_1 = [2, 3, 4]
numbers_2 = [20, 30, 40]

final = []

for i in numbers_1:
    for j in numbers_2:
        final.append(i+j)

print(final)    ### [22, 32, 42, 23, 33, 43, 24, 34, 44]





## Single Line Nested Loops Using List Comprehension

first = [2, 3, 4]

second = [20, 30, 40]

final = [i+j for i in first for j in second]

print(final)


## for x in first: [print(x+y) for y in second]

## exec("for x in first:\n    for y in second:\n        print(x+y)")