# If, Else, and Elif Problems:


"""

For this problem you are going to make a program that simulates the output of a vending machine that only takes in
coins of American currency.

1.Your program should take an integer as an input from the user (either a 1, 2, or 3) that corresponds with an option
for a drink from the vending machine outlined below and assign the corresponding price to a variable as a float.
Use your knowledge of if, elif, and else statements to complete this part of the problem.  Your code should
have an else statement that prints a message and ends the program using sys.exit() if the user does not enter a valid
input number.

   Vending Machine:
   1.water = $1.00
   2.cola = $1.50
   3.gatorade = $2.00

2.After placing an order, the user should be prompted to enter inputs 4 times:
1.The first time, the user should be prompted to enter the number of quarters they put in the machine.  Assign this
number to a variable as an integer.
2.The second time, the user should be prompted to enter the number of dimes they put in the machine.  Assign this
number to a variable as an integer.
3.The third time, the user should be prompted to enter the number of nickles they put in the machine.  Assign this
number to a variable as an integer.
4.The fourth time, the user should be prompted to enter the number of pennies they put in the machine.  Assign this
number to a variable as an integer.

3.Create a variable to hold the total value of all the coins the user has put into the machine.

4.Use flow control statements to print the user's change or output a message asking the user to try again depending
on whether the total value of the coins the user has put into the machine is enough to pay for the item they ordered.

New knowledge for this problem:
1.%f format specifier
2.import sys and sys.exit()
3.int()

"""
import sys

order = int(input("Enter your order number as an integer.(1, 2, or 3"))

if order == 1:
    disPrice = 1.00
elif order == 2:
    disPrice = 1.50
elif order == 3:
    disPrice = 2.00
else:
    sys.exit("Please try again.")

quarters = int(input("Enter the number of quarters as an integer."))
dimes = int(input("Enter the number of dimes as an integer."))
nickels = int(input("Enter the number of nickels as an integer."))
pennies = int(input("Enter the number of pennies as an integer."))

total = quarters * .25 + dimes * .10 + nickels * .05 + pennies * .01

if total >= disPrice:
    print("Your change is $" + "%.2f" % (total - disPrice) + ". Have a nice day.")
else:
    print("Please try again.")