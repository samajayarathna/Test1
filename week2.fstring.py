#Write a script that takes in three integers as input from a user and displays them equally spaced across the screen 
# using an f-string.

num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))
num3 = int(input("Enter third number"))

print(f"{'first' :28} {'second' : ^28} {'third' : >28}")
print(f"{num1 : <28} {num2 : ^28} {num3 : >28}")

