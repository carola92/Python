"""" 
Variables and Data types review
1.create a variable called intVal and assign it an integer value
2.create a variable called floatVal and assign it a float value
3.create a variable called boolVal and assign it a boolean value
4.use print() to display the Boolean value assigned to BoolVal in the output of the program
5.reassign boolVal a differen Boolean value than the one assigned to it in step 3
6.use print() to display the integer value assigned to intVal in the output of the program
7.use print() to display the float value assigned to floatVal in the output of the program
8.use print() to display the Boolean value reassigned to boolVal in the output of the program
"""

intVal = 5

floatVal = 2.21

boolVal = False

print(boolVal)

boolVal = True

print(intVal)

print(floatVal)

print(boolVal)
#_________________________________________________________________________________________________________
""""
Comments and Math Operators review
Comments:
1.create a single Line comment
2.create a multiple Line comment
Math Operators:
3.create a variable called add and assign it the sum of two integers
4.create a variable called sub and assign it the difference of two integers
5.create a variable called div and assign it the quotient of two integers
6.create a variable called prod and assign it the product of two integers
Assignment Operators:
7.Create 3 variables called operators 1, operators2, and operators3 and assign them all the value 2
8.use the exponation assignment operator to reassign operators 1 the value 4
9.use the floor division assignment to reassign operators 2 the value 4.0
10.use the modulo assignment operator to reassign operators 3 the value 0
output:
11.use print() to display the values assigned to the variables add, sub, div, and prod on one line in the output when the program is run
12.use print() to display the values reassigned to the variables operators1, operators2, and operators3 on the same line in the output when the program is run
"""
# this is a single line comment

"""

This is a multiple line

comment

"""

add = 3 + 2
sub = 9 - 6
div = 10 / 5
prod = 4 * 7

operators1 = 2
operators2 = 2
operators3 = 2

operators1 **= 2
operators2 //= 0.5
operators3 %= 1

print(add, sub, div, prod)
print(operators1, operators2, operators3)

# ____________________________________________________________
""""
# Strings and Escape Sequences review
1.print a string surrounded by single quotes
2.print a string surrounded by double quotes
3.use an escape sequence to surround the "in quotes" from the string "This should be in quotes." in double quotes
4.create a variable and assign it the string "Alligator"
5.access the "a" in "alli" from the variable created in step 4
6.print the slice "Alli" from the variable created in step 4
7.print the slice "gat" from the variable created in step 4
8.print the slice "tor" from the variable created in step 4
"""
print('single quotes')
print("double quotes")

print("this should be \"in quotes\".")

gator = "Alligator"

print(gator[5])

print(gator[:4])

print(gator[4:7])

print (gator [6:])

#________________________________________________________________
"""
String Methods revieuw
1.print the length of the string "Manchester United"
2.convert the integer 12345 to a string then access and print "3" from the new string
3.use .upper() to make all the characters in the string "albania" upper case. Print the new string of all capital
letters.
4.use .lower() to make all the characters in the string "BELGIUM" lower case. Print the new string of all lower case
letters
"""
print(len("Manchester United"))

print(str(12345)[2])

print("albania".upper())

print("BELGIUM" .lower())

#_______________________________________________________________
""""
print() review
1.Use input() to prompt the user to enter their name when the program is run. Assign what is entered to a variable
called name.
2.Print the user's name using the %s operator concatenated to the end of the string "Your name is ". Example: the
user enters John for their name. The output should be "Your name is John"
"""
name = input("Please enter your name.")

print("Your name is " +  "%s" % (name))

#______________________________________________________________
""""
Flow Control and Comparators review

For This review exercise, just guess whether each statement in the parentheses
of print evaluates True or False
"""

print(8 > 8)
print(6 <= 6)
print(5 < 5)
print(10 != 10)
print(4 == 5)
print(7 >= 7)
print(7!= 9)
print(5 < 9)
print(20 <= 6)
print(5 > 6)
print(3 == 3)
print(2 >= 1)

#_______________________________________________________________
""""
Boolean Operators review

For this review excercise, guess whether the statements in the
parentheses of print evaluate to True or False
true, true, false, true
"""

print(7 > 6 and 6 >= 6)
print(3 != 3 or 4 == 4)
print(not 5 > 2)
print(not 5 < 3 and True or 6 <= 6 and not False)

#______________________________________________________________
""""
If, Else, and Elif review
1.Use input() to get the user's name and assign it to a variable.
2.Assign the length of the user's name to a variable.
3.Using your knowledge of If, Else and Elif statements, create a set of statements that 
print "your name is less that 4 characters" if the user's name is less than 4, prints
"your name is at least 4 characters and less that 10 characters" if the user's namee is greater
than or equal to 4 characters in length but less than 10 characters long, and prints "your name
is very long" if the user's name does not trigger the other statements.
"""

name = input("Enter your name")

nameLen = len(name)

if nameLen < 4:
    print ("Your name is less than 4 characters")
elif nameLen < 10:
    print ("Your name is at least 4 characters and less than 10 characters")
else:
    print ("Your name is very long")

#____________________________________________________________________________________
"""
Functions review
1.create a function which takes zero parameters and prints "this is a function" when called
2.create a function which will take an integer as a parameter and returns it after
multiplying it by 2
3.create a function that takes two parameters, one will be the function you made in step 2,
and the other will be another integer. The function should return the product of its two
inputs.
4.Create a function that takes three parameters. It should call the function you made in 
step 3. The first of the function you made in step 3's inputs should be a call of the 
function you made in step 2 with the first of the three parameters of the function you
are making for step 4 as its input. The second input parameter of the function you made 
for step 3 should be the same as the second input parameter you are using for the function
you are making for step 4. Then, the call of the function you made in step 3 should be
multiplied by the third parameter you used for the function you are making for step 4.
Finally, this entire thing should be printed.
5.call the function you made in step 1
6.call the function you made in step 4 with 7, 4, and 2 for its inputs. 112 should be the result.
"""

def first():
    print("this is a function")

def intFun(intVal):
    return intVal * 2

def takesTwo(int1, int2):
    return int1 * int2

def functionInside(a, b, c):
    print(takesTwo(intFun(a), b) * c)

first()

functionInside(7, 4, 2)

#____________________________________________________________________________________
"""
Importing Modules review
1.use a generic import to import the random module
2.use a function import to import the randint function from the random module
3.use a universal import to import everything from the math module
4.use the randint function to generate a random number greater than or equal to 5 and less
than or equal to 10. Print this number.
5.use the factorial() function to print the factorial of 4(factorial() is a function that
should be imported if you correctly used universal import on the math module)
6.call the random() function (imported when you used generic import on the random module) with
no input parameter. This will generate a float that is greater than or equal to 0.0 and less
than 1.0. Print the call of the random() function.
"""

import random
from random import randint
from math import *

print(randint(5, 10))

print(factorial(4))

print(random.random())

#________________________________________________________________________________________
"""
Built-In Functions review
1.use the abs() function to get and print the absolute value of a negative integer.
2.use the type() function to get and print the type of a float
3.use the max() function to get and print the max() of the following numbers: 1, 9, 2, 3, 20
4.use the min() function to get and print the min() of the following strings: "bca", "cde", "fgh"
"""
print(abs(-2))

print(type(5.678))

print(max(1, 9, 2, 3, 20))

print(min("bca", "cde", "fgh"))

#_______________________________________________________________________________________
"""
Lists review
1.create a variable and assign it the list [1, 2, 3, 4, 4, 6]. Print the list.
2.reassign the index which is currently assigned the second 4 in the list the integer 5. Print the new list.
3.use .append() to add 7 to the end of the list and print the new list.
4.print the slice [1, 2, 3, 4] from the list you made in step 3.
5.print the slice [3, 4, 5] from the list you made in step 3.
6.print the slice [6, 7] from the list you made in step 3.
7.use .index() to get and print the index of the integer 7 from the list you made in step 3.
8.use .insert() to insert 0 at index 0 of the list you made in step 3. Print the new list.
9.use .remove() to remove 3 from the list you made in step 8. Print the new list.
10.use .pop() to remove and print the last item from the list you made in step 9.
11.print the new list that results from step 10. 
"""
listVal = [1, 2, 3, 4, 4, 6]
print(listVal)

listVal[4] = 5
print(listVal)

listVal.append(7)
print(listVal)

print(listVal[:4])
print(listVal[2:5])
print(listVal[5:])

print(listVal.index(7))

listVal.insert(0, 0)
print(listVal)

listVal.remove(3)
print(listVal)

print(listVal.pop())

print(listVal)

#_______________________________________________________________________________________
"""
For loops and Tuples Review
1.create a variable and assign it a tuple comprised of 4 integers.
2.access the second integer from the tuple you assigned to a variable in step 1 and print it.
3.print a slice comprised of the first 2 integers from the tuple from step 1.
4.print a slice comprised of the middle 2 integers from the tuple from step 1.
5.print a slice comprised of the last 2 integers from the tuple from step 1.
6.use a for loop to iterate through the tuple from step 1 and print all of its elements on different lines
in the output.
"""
tupVal = (4, 3, 2, 1)

print(tupVal[1])

print(tupVal[:2])
print(tupVal[1:3])
print(tupVal[2:])

for num in tupVal:
    print(num)

# _______________________________________________________________________________________
"""
Dictionaries review
1.create an empty dictionary and assign it to a variable.
2.add 3 key: value pairs to the dictionary from step 1 and print the new dictionary.
3.get and print the length of the dictionary you made in step 2.
4.access a value by key from the dictionary you made in step 2 and print it.
5.reassign a key from the list you made in step 2 a different value and print the new value.
6.use del to remove a value from the list you made in step 5, then print the resulting list.
"""
emp = {}

emp["first"] = 2
emp["second"] = 3
emp["third"] = 4
print(emp)

print(len(emp))

print(emp["first"])

emp["first"] = 10
print(emp["first"])

del emp["second"]
print(emp)

# _______________________________________________________________________________________
"""
Using Functions with Lists review
1.create a variable and assign it a list comprised of 3 strings
2.define a function that takes one input (this input will be a list.)
3.make the function you defined in step 2 print the second element of the list used as its input.
4.make the function you defined in step 2 concatenate the string "frog" to the third element of the list used as its
input then print the element.
5.use the remove() function to remove the first element from the list that the function defined in step 2 is using as
its input and within the function, print the resulting list.
6.call the function you made in steps 2-5 with the list you made in step 1 as its input.
"""
inList = ["jump", "leap", "hop"]

def one_li(list_val):
    print(list_val[1])
    print(list_val[2] + "frog")
    list_val.remove(list_val[0])
    print(list_val)

one_li(inList)

# _______________________________________________________________________________________
"""
Using An Entire List Within A Function review
1.create a list of 4 integers and assign it to a variable
2.create a function that takes a list as an input and prints that list's elements using a for loop.
3.create 3 lists using range() and assign each of them to a different variable. The three lists should be as follows:
[0, 1, 2], [2, 3, 4], and [2, 7, 12].
4.create a function that takes 3 lists as parameters, sums their contents using range() and a for loop and returns a
list comprised of the summed numbers. For example, if the function was called with the lists [1,2], [0,1], and
[3,4] as inputs, it would take 1, 0, and 3 and add them together and then it would take 2, 1, and 4 and add them
together. The resulting sums 4 and 7 would be returned as the list [4, 7]. (the 3 inputs lists will all be the same
length.)
5.create a function that iterates through and prints the items of each list in a list of lists using for loops.
6.call the function you made in step 5 with the list of lists [[1,2], [0,1], [3,4]] as its input.
7.call the function you made in step 2 with the list you made in step 1 as its input.
8.print a call of the function you made in step 4 with the lists you made in step 3 as its inputs.
"""
fourInts = [7, 5, 3, 1]

def printer(list_val):
    for items in list_val:
        print(items)

first = range(3)
second = range(2, 5)
third = range(2, 13, 5)

def sum_lists(list1, list2, list3):
    new_list = []
    for items in range(0, len(list1)):
        new_list.append(list1[items] + list2[items] + list3[items])
        return new_list

def LOL_printer(LOL):
    for items in LOL:
        for num in items:
            print(num)

LOL_printer([[1,2], [0,1], [3,4]])

printer(fourInts)

print(sum_lists(first, second, third))

# _______________________________________________________________________________________
"""
While Loops review
1.import the randint function from the random module
2.create a variable called counter and assign it the value 5.
3.create a while else loop that prints counter while counter is less than 10, has a break statement that prints a 
message if counter is equal to 7, assigns counter a new random integer that is greater than or equal to 5 and less
than or equal to 10 each time counter is less than 10 and not equal to 7, and has an else statement that prints a
message if counter is equal to 10.
"""
from random import randint

counter = 5

while counter < 10:
    print(counter)
    if counter == 7:
        print("Counter is equal to 7.")
        break
    counter = randint(5, 10)
else:
    print("counter is equal to 10.")

# _______________________________________________________________________________________
"""
More For Loops review
1.create a variable and assign it a string.
2.create a variable and assign it a list of integers.
3.create a variable and assign it a dictionary.
4.iternate through and print the characters from the string you made in step 1 using range() and a for loop.
5.using a for loop, iterate through the items from the list you made in step 2 and print them on the same line.
6.use a for loop to iterate through and print the values from the dictionary you made in step 3.
7.create a list of integers of the same length as the one you made and print the larger elements out of the two of them.
8.use a for loop to iterate through both of the lists you made and print the larger elements out of the two of them.
  For example, if your lists are [4, 1, 2] and [6, 2, 9], the for loop would print 4, 2, and 9. If and element from
  one of the lists is equal to the other, your for loop should print the element from the first list. (Your for loop
  should also use the zip() function.)
9.use a for/else loop to iterate through and print the values from the list you made in step 2 on the same line. Use
    the else statement to print another integer.
"""
strVal = "Bilbo Baggins"

listVal = [1, 2, 3, 4]

dictVal = {1: "one", 2: "two", 3: "three"}

for char in range(0, len(strVal)):
    print(strVal[char])

for items in listVal:
    print(items, end = "")

for key in dictVal:
    print(dictVal[key])

otherList = [4, 2, 2, 1]

for num1, num2 in zip(listVal, otherList):
    if num1 > num2:
        print(num1)
    elif num2 > num1:
        print(num2)
    else:
        print(num1)

for elements in listVal:
    print(elements, end = "")
else:
    print(5)

# _______________________________________________________________________________________
"""
List Comprehensions review
1.Create the list [1, 3, 5, 7, 9] using a list comprehension without an if statement and print it.
2.Create the list [3, 4, 5, 6, 7] using a list comprehension without an if statement and print it.
3.Create the list [3, 4, 5, 6, 7] using a list comprehension with an if statement and print it.
4.Create the list [3, 4, 5, 6, 7] using a list comprehension with an if statement and print it.
"""
print([num1 for num1 in range(1, 10, 2)])
print([num2 for num2 in range(3, 8)])
print([num3 for num3 in range(1, 10) if num 3 % 2 == 1])
print([num4 for num4 in range(8) if num4 > 2])

# _______________________________________________________________________________________
"""
List Slicing With Stride review
1.create a variable and assign it the list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
2.print the slice [2, 4, 6, 8, 10, 12, 14, 16, 18] from the list you made in step 1
3.print the slice [1, 6, 11, 16] from the list you made in step 1
4.print the slice [12, 9, 6, 3] from the list you made in step 1
5.print the reverse of the list you made in step 1
"""
listVal = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print(listVal[1:18:2])
print(listVal[::5])
print(listVal[11:1:-3])
print(listVal[::-1])

# _______________________________________________________________________________________
"""
Try And Except review

the problem:
Create a program using your knowledge of Try and Except statements which compares two integers: one which is a user
entered integer (use input() for this) and another which is a randomly generated integer that is greater than or
equal to 0 and less than nor equal to 5. Print the random integer. The program should compare the two integers and
print the larger of the two. It should print a message saying that the numbers are the same if they are equal. The
program should also have an exception that prints a message if the user does not enter something that can be converted
to an integer.
"""
from random import randint
rand = randint(0, 5)
print(rand)

userNum = input("Enter an integer")

try:
    if rand > int(userNum):
        print(rand)
    elif int(userNum) > rand:
        print(int(userNum))
    else:
        print("The numbers are the same.")
except:
    print("Please run the program again and enter an integer.")
# _______________________________________________________________________________________
