# Lists and Tuples

## Lists

### char lists
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']


### string lists
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

### integer lists
squares = [1, 4, 9, 16, 25]


### decimal lists
numbers = [66.25, 33.3, 6.45, 1234.5]

### mixed lists
mixed = [1, "Hello", 3.4]

### list of lists
Mylist = [letters,fruits,numbers]


### nested list
nested = ["hehe", [8, 4, 6], ['a']]

### empty list
my_list = []


print(fruits) #### ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

print(fruits[0]) #### orange

print(fruits[0:3]) #### ['orange', 'apple', 'pear']

print(fruits[-2]) #### apple




## 2D Lists

### each item in a list is an another list.

matrix = [
            [1, 2, 3], 
            [4, 5, 6],
            [7, 8, 9]
         ]

#### matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

#### get the first item
f = matrix[0] ##### [1, 2, 3]

#### get the first item's second item
s = matrix[0][1] ##### 2

print(fruits[0][1]) #### means orange[1] = r




"""
Lists can be modified.
"""


fruits.append(6)  #### adds 6 at the and of the list  - ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana', 6]   

fruits.insert(0, 20) #### adds 20 to index 0 -- [20, 'orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana', 6]

fruits.remove('pear') #### removes the value 'pear' from the list  - [20, 'orange', 'apple', 'banana', 'kiwi', 'apple', 'banana', 6]       

fruits.pop()  #### removes last item - [20, 'orange', 'apple', 'banana', 'kiwi', 'apple', 'banana']

print(fruits.index('banana')) #### returns the index  -- 3 

print(50 in fruits) #### checks the existence -- False

print(fruits.count('banana')) #### Return number of occurrences of value --- 2

fruits[0] = 52

print(fruits) #### [52, 'orange', 'apple', 'banana', 'kiwi', 'apple', 'banana']

#fruits.clear()  #### removes all the items from the list -- []


print(numbers.sort())  #### Sort the list in ascending order and return None.

print(numbers)  #### [6.45, 33.3, 66.25, 1234.5]

numbers.reverse()  #### Reverse the list

print(numbers) #### [1234.5, 66.25, 33.3, 6.45]

numbers2 = numbers.copy() #### Return a shallow copy of the list.

print(numbers2) #### [1234.5, 66.25, 33.3, 6.45]




# Tuples

"""
Tuples cannot be modified.
"""


fruits_tuple = ("apple", "banana", "cherry")

num_tuple = (1, 2, 3, 4, 5, 4, 2 , 4)

asdfasd = ( (12345, 54321, 'hello!'), (1, 2, 3, 4, 5) )

print(num_tuple)  ### (1, 2, 3, 4, 5, 4, 2, 4)

print(num_tuple[-2])  ### 2

print(num_tuple.count(4))  ### 3

"""
num_tuple[0] = 1 ### this will raise an error
"""
