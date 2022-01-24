#Create a script that takes a single integer as input from a user and compares it to a hard-coded number. 
# Use a if, elif, else block to determine if the input is less than, higher than or, equal to the hard-coded number. 
# Put everything in a while loop so the user can have multiple attempts at guessing the hard-coded number until
#  they get it correct.

from pickle import TRUE


num1 = int(input("Enter an integer value"))
num2 = 10
x=0
while TRUE:
    if num1 < num2:
        print("number is less than to actual number")
    elif num1 > num2:
        print("number is higher than the actual number")
    else:
        print("your number is equal to actual number")
        break
    x  += 1
    