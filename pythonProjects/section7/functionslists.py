"""


0.Setup:
a.create a list of integers and assign it to a variable
b.create a list of strings and assign it to a variable
c.create a list of floats and assign it to a variable


1.Passing A List to A Function:
a.create a function that takes and returns an input
b.print a call of the function you created in step 1.a. with the list of integers from step 0.a. as the input
c.print a call of the function you created in step 1.a. with the list of strings from step 0.b. as the input
d.print a call of the function you created in step 1.a. with the list of floats from step 0.c. as the input


2.Accessing An Element In A list using A Function:
a.create a function that takes a list as an input and returns one of that lists elements
b.print a call of the function you created in step 2.a. with the list of integers from step 0.a. as the input
c.print a call of the function you created in step 2.a. with the list of strings from step 0.b. as the input
d.print a call of the function you created in step 2.a. with the list of floats from step 0.c. as the input


3.Modifying A List Element Within A Function:
a.create and call a function that prints the product of all the integers from the list you created in step 0.a.
b.create and call a function that concatenates all the strings from the list you create in step 0.b and prints the
result
c.create and call a function that prints the quotient of all the floats from the list you created in step 0.c.

4.Manipulating Lists Within Functions:
a.create a list that uses 3 of the following functions on one of the lists you created in part 0 of this problem set:
.index(), .append(), .remove(), .insert, or .pop(). Also, make sure that the function prints the resulting list
b.call the function from part 4.a. using one of the lists you made in part 0 of this problem set.

"""
0.
Nrs = [1, 2, 3, 4, 5]
Ltrs = [a, b, c, d, e]
Flts = [0.5, 1.5, 2.5, 3.5, 4.5]

1a.
def list_passer(li):
    return li

1bcd.
print(passer(Nrs))
print(passer(Ltrs))
print(passer(Flts))

2a:
def access(theList):
    return theList[1]

2.bcd:
print(access(Nrs))
print(access(Ltrs))
print(access(Flts))

3a:
def product(a):
    print(a[0]*a[3])
product(ints)

3b:

def ​concatenator(b)
 holder = ​""
for ​x ​ in ​b:
    holder += x
​print​(holder)

concatenator(strings)

3c:
def ​quotient(c):     ​
print​(c[​2​] / c[​1​])
 quotient(floats)  ​

4.