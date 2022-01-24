
from logging import exception


# try:
#     x= int(input("Enter a number: "))
#     print(x)
# except ValueError:
#     print("only numbers are valid for input")

# except FileNotFoundError:
#     print("That's an error. try again")

# finally:
#     print("something went wrong")

#Write a script that takes two numbers from the command line and using an if statement, displays which one is greater. 
# If the numbers are equal "they are equal" is to be displayed

#Put the script into a while loop so that it repeats unless 'q' is entered
#use a ValueError exception to catch if a letter is entered as either of the input numbers, rather than a number

z=0
while True:
    try:
        num1 = int(input("Enter first number"))
        num2 = int(input("Enter second number"))

        if num1 < num2:
            print(num2,"second number is greater than first number")
            elif:
                num2 > num1:
                print(num1,"first number is greate than second number")
                else:
                    print(" both numbers are equal")
                    z= input("Any key to repeart or \'q\' to quit")
    if z == 'q':
        break

except ValueError:
    print("Only numbers are valid")

