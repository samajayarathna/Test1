# Create a menu with three options. 1. Add numbers; 2. Subtract numbers. 3. Exit
# If option 1 is chosen a function should be called that asks for input of two numbers, adds them, displays the result 
# and returns to the menu
# If option 2 is chosen a function should be called that asks for input of two numbers, subtracts them, displays the 
# result and returns to the menu
# If option 3 is chosen the program should exit.
# If any other input is entered the menu simply repeats

def sum():
    x = int(input("enter a number "))
    y = int(input("enter a number "))
    print(x + y)

def subtraction():
    x = int(input("enter a number "))
    y = int(input("enter a number "))
    print(x - y)
    x = 0

y= 0
while y != 3:
    print("enter 1 to add two values")
    print("enter 2 to subtract two values")
    print("enter 3 to quit")
    y = int(input("Choose an option"))
    if y == 1:
        sum()
    elif y == 2:
        subtraction()
