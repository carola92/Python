"""

Single parameter and zero parameter functions:
1.define a function that takes no parameters and prints a string
2.create a variable and assign it the value 5
3.create a function that takes a single parameter and prints it
4.call the function you created in step 1
5.call the function you created in step 3 with the variable you made in step 2 as its input

"""

# ----------------------------------------------------------------------------------------------------------------------
1.
def none():
   print("string")
2.
Var = 5
3.
def Para (p):
    print(p)
4.
none()
5.
Para(Var)
# ----------------------------------------------------------------------------------------------------------------------

""" 

multiple parameter functions: 
1.create 3 variables and assign integer values to them 
2.define a function that prints the difference of 2 parameters 
3.define a function that prints the product of the 3 variables 
4.call the function you made in step 2 using 2 of the variables you made for step 1 
5.call the function you made in step 3 using the 3 variables you created for step 1 

"""

# ----------------------------------------------------------------------------------------------------------------------
1.
int1, int2, int3 = 1, 2, 3
2.
def diff(a,b):
    print(a-b)
3.
def prod(c,d,e):
    print(c*d*e)
4.
diff(int1,int2)
5.
prod(int1,int2,int3)
# ----------------------------------------------------------------------------------------------------------------------

""" 

Calling previously defined functions within functions: 
1.create 3 variables and assign float values to them 
2.create a function that returns the quotient of 2 parameters 
3.create a function that returns the quotient of what is returned by the function from the second step and a 
third  parameter 
4.call the function you made in step 2 using 2 of the variables you created in step 1.  Assign this to a variable. 
5.print the variable you made in step 4 
6.print a call of the function you made in step 3 using the 3 variables you created in step 1 

"""

# ----------------------------------------------------------------------------------------------------------------------
1.
Var1, Var2, Var3 = 5.55, 3.25, 6,87
2.
def div(a, b):
    return a/b
3.
def div2(c, d, e)
    return div(c,d)/e
4.
step2func = div(Var1, Var2)
5.
print(step2func)
6.
print(div2(Var1, Var2, Var3))
# ----------------------------------------------------------------------------------------------------------------------