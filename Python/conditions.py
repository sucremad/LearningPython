# If Statements

"""
What if we want to do something only in a certain condition?
"""

isHot = True

if isHot:
    print("It is a hot day!")  ## this will print "It is a hot day!"


"""
here indentation is important!!!

indentation means this codes are in the if block so they will run according to if statement

if you dont use indentation it will run indepently from if block

and if block works while the condition is met. Otherwise it will be ignored.
"""    



isHot = False

if isHot:
    print("It is a hot day!")  ## this will print nothing bcs condition is not met

if isHot:
    print("It is a hot day!")   
print("Enjoy..")  ## this will print just  "Enjoy.." bcs it is not in if block.



"""
What if we want to do something only in a certain condition, otherwise another thing?
"""


"""Comparison Operators

==	    Equal	                    x == y	
!=	    Not equal	                x != y	
>	    Greater than	            x > y	
<	    Less than	                x < y	
>=	    Greater than or equal to	x >= y	
<=	    Less than or equal to	    x <= y


"""   



age = 22

if age < 18:       ## if ur age under 18, u cannot come in 
    print("You cannot enter..")
else:              ## otherwise u can.
    print("You are allowed to enter..")

## This will print "You are allowed to enter.." bcs age greater than 18.



"""
What if we want to do different things under different conditions?
"""

### Infant = 0-1 year.
### Toddler = 2-4 yrs.
### Child --> 5-12 yrs.
### Teen --> 13-19 yrs.
### Adult --> 20-39 yrs.
### Middle Age Adult = 40-59 yrs.
### Senior Adult = 60+


age_stage = None

if age <= 1:
    age_stage = "Infant"
elif 2 <= age < 5:
    age_stage = "Toddler"
elif 5 <= age <=12:
    age_stage = "Child"
elif 12 < age <= 19:
    age_stage = "Teen"
elif 20 < age <= 39:
    age_stage = "Adult"
elif 40 <= age < 60:
    age_stage = "Middle Age Adult"
else:
    age_stage = "Senior Adult"  


print(f"Your age stage is {age_stage}")     ### Adult



## Logical Operators


"""
and --> only Returns True when all conditions are true
or  --> Returns True if one of the statements is true
not --> Reverse the result
"""

isFemale = True
isTall = False


if isFemale and isTall:
  print("You are a tall Female")
else:
  print("You either not female or not tall or both")

### prints "You either not female or not tall or both" bcs isTall is False



if isFemale or isTall:
  print("You are a female or tall or tall Female ")
else:
  print("You are not female and not tall")

### prints "You are a female or tall or tall Female" bcs isFemale is True



isMan = True
isSad = True

if not isSad and not isMan:
    print("Happy Woman")
else:
    print("Sad Man")





