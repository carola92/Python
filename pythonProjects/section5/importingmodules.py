"""

Importing Modules:
1.Use a generic import to import the "random" module
2.Use a universal import to get everything from the "math" module
3.Use a function import to get the exit() function from the "sys" module
4.Use a function from the random module to generate a float greater than or equal to 0 and less than 100 and
assign that number to a variable
5.use the sqrt() function from the math module to get the square root of the number from step 4 and assign that to a
variable
6.call the exit() function from the sys module with the variable from step 5 as what it will display

"""

1.
import random
2.
from math import *
3.
from sys import exit
4.
rand = random.rand() * 100
5.
square= sqrt(rand)
6.
exit(square)