"""

comments practice:

1.create a single line comment
2.create a multiple line comment

"""

# enter your code for "comments practice" between this line and the line below it---------------------------------------

# this is a single line comment

""""

This is 
 
a multiple 

line comment

"""

""" basic mathematical operators practice: 
1.create a variable called add and assign it the sum of two numbers 
2.create a variable called sub and assign it the difference of two numbers 
3.create a variable called mult and assign it the product of two numbers 
4.create a variable called div and assign it the quotient of two numbers 
5.create a variable called power and assign it the value of a number raised to a power 
6.create a variable called mod and assign it the remainder of a quotient 
"""

# enter your code for "basic mathematical operators practice" between this line the line below it-----------------------

add = 3 + 2

sub = 5 - 4

mult = 5 * 2

div = 7 / 2

power = 4 ** 2

mod = 7 % 5

# ----------------------------------------------------------------------------------------------------------------------

""" modulo practice: 
1.create a variable called mod1 and assign it the result of 7 % 5 
2.create a variable called mod2 and assign it the result of 16 % 6 
3.create a variable called mod3 and assign it the result of 4 % 3 """

# enter your code for "modulo practice" between this line and the line below it-----------------------------------------

mod1 = 2

mod2 = 4

mod3 = 1

# ----------------------------------------------------------------------------------------------------------------------

""" order of operations practice: 1.create and assign a variable called ordOp1 the result of 7 + 6 + 9 - 4 * ((9 - 2) ** 2) / 7 2.create and assign a variable called ordOp2 the result of (6 % 4 * (7 + (7 + 2) * 3)) ** 2 """

# enter your code for "order of operations practice" between this line and the line below it----------------------------

# Original Expression: 7 + 6 + 9 - 4 * ((9-2) ** 2) / 7
# Step 1 Parentheses: 7 + 6 + 9 - 6 * (7**2) / 7 then 7 + 6 + 9 - 4 * 49 / 7
# Step 2 Multiplication and Division from left to right: 7 + 6 + 9 - 196 / 7 then 7 + 6 + 9 - 28
# Step 3 Addition and Subtraction from left to right: 13 + 9 - 28 then 22 - 28 and finally, -6
ordOp1= -6

# Original Expression: (6 % 4 * (7 + (7 + 2) * 3 )) ** 2
# Step 1 Inner Parentheses: (6 % 4 * (7 + 9 *3)) ++2
# Step 2 Multiplication within innermost parentheses: (6 % 4 * (7+27)) ** 2
# Step 3 Addition within innermost parentheses: (6 % 4 * 34) ** 2
# Step 4 Modulo and Multiplication within Parentheses from left to right: (2*34) ** 2 than 68 ** 2 and finally, 4624
ordOp2 = 4624
# ----------------------------------------------------------------------------------------------------------------------

