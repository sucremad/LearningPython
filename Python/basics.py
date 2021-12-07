# Let's get starteeed

# ---------  PYTHON BASICS -------------


# Comments

# This is one line Comment

"""
This is 
multine line comment
Both of them does nothing
Just gives info about your code
or whatever u want
"""

# printing

print("Hello world!")
print('Hello World!')

print("""Yeah,
        Multiple Liness!!
      """)

print('''another alternative
        for Multiple Liness!!
      ''')


# Variables and data types

## String 

name = "Nop"
last_name = "Con"
age = "22"

## Number

my_age = 21 ### integer
gpa = 3.62  ### float



### Arithmetic Operations


addition = 10 + 3 

"""
addition :
x = 10
x = x + 3 ----> now x = 13

same as:

x += 3   (shorter form)

it can be used with other operations: 

x += 3
x -= 3
x /= 3


"""
subtraction = 10 -3
multiplication = 10 * 3
division1 = 10 / 3      #### result as decimal  - 3.3333
division2 = 10 // 3     #### result as integer  - 3
modulus = 10 % 3        #### returns remain of the division - 1
exponent = 10 ** 3      #### power



## boolean
### Only True or False

isHappy = True
isDepressed = False


print("My name is ", name)
print("My last name is " + last_name)
print(my_age)
print(gpa)




# Taking input

## it takes input as a string

# username = input("What is your username? : ")

# print('Hello ', username, '!')



# Type Conversion

## int()    ---- turns into integer
## float()  ---- turns into float
## bool()   ---- turns into boolean
## str()    ---- turns into string


birth_year = input("What is your birth year? : ") 

# bcs of it takes input as a string, u cannot subtract int/float from a string.
# So u need to convert it to int/float

your_age = 2021 - int(birth_year)

"""
or direcly convert after input:

birth_year = int(input("What is your birth year? : "))

your_age = 2021 - birth_year


"""


"""
print("My GPA is " + gpa)

This gonna raise an error because it cannot concetenate string and float/int.
You need to convert it to string.

""" 


print("My GPA is " + str(gpa))
print("Your age is " + str(your_age))





# Working with Strings


#  +---+---+---+---+---+---+
#  | P | y | t | h | o | n |
#  +---+---+---+---+---+---+
#  0   1   2   3   4   5   6
# -6  -5  -4  -3  -2  -1


"""
indexes begin from 0 (zero) in the strings.
this indicates how far the char is from the beginning.

when we want it from the end, it starts from -1.
"""

print("Learning\nPython")  ## \n means go to new line

sentence = "Hey guys 1 am hereee!"

print(sentence.upper())  ## prints it fully uppercase
print(sentence.lower())  ## prints it fully lowercase

print(sentence.isupper())  ## prints if sentence enterily upper


print(sentence.find('e'))  ## prints the first index of 'e'  --- 1

print(sentence.find('er'))  ## prints the first index of 'er' --- 15
print(sentence.index('er'))  ## prints the first index of 'er' --- 15


print(sentence.replace('1', 'I'))  ## this function replaces '1' with 'I' in the sentence

print(sentence.replace('guys', 'folks'))  

print('guys' in sentence)  ## it checkes if sentence contains 'guys' --- False or True


print(len(sentence))  ## prints the lenght of sentence

print(sentence.split(' ')) # prints the sentence by splitting spaces

splitted_sentence = sentence.split(' ')  ## ['Hey', 'guys', '1', 'am', 'hereee!']
 
print(splitted_sentence[1]) ## prints 'guys'

splitted_sentence[1].capitalize()  ## Converts the first character to upper case --- 'Guys' 


any_string= " bla bla "
print(any_string.strip()) ## removes any whitespace from the beginning or the end --- 'bla bla'


print(sentence.title())  ## Converts the first character of each word to upper case


print("nom" * 3)  ## nomnomnom

python = 'Py' 'thon'  ## python = 'Python'

print(python)  ## 'Python'


## nth character

### sentence[n-1]
### why n-1?
### bcs indexes start from 0


first_character = sentence[0]  # H

third_character = sentence[2]  # y

last_character = sentence[-1]  # !

print(last_character)

print(sentence[0:3]) # prints from index 0 to index 3 (index 3 not included)   ---- 'Hey'

print(sentence[:3]) # prints from index 0 to index 3 (index 3 not included)  ---- 'Hey'

print(sentence[2:3]) # prints from index 3 to index 3 (index 3 not included) ---- 'y'

print(sentence[4:]) # prints from index 5 to the end ---- 'guys 1 am hereee!'

print(sentence[:]) # prints from the beginning to the end ---- 'Hey guys 1 am hereee!'


print(sentence[1:-1]) # prints from index 1 to index -1 (index -1 not included) ---- 'ey guys 1 am hereee'

print(sentence[-3:]) # prints from the index -3 to the end ---- 'Hey guys 1 am hereee!'





### Formatted Strings


first_name = "Willie"
last = "Wonka"

message = f'{first_name}\'s last name is {last}'
message2 = '{0}\'s last name is {1}'.format(first_name, last)
message3 = '{nop}\'s last name is {yep}'.format(nop=first_name, yep=last)



print(message) 
print(message2)
print(message3) ## "Willie's last name is Wonka"


pi_value = 3.14159

print(f'The value of pi is {pi_value:.3f}.') ## prints 'The value of pi is 3.142.'

