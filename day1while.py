#Create a script that takes an integer as input from the user and
#  increments it five times using a while loop and, displays the 
# result

#method 1
x = int(input("enter first number"))
y = x
while y < (x+5) :
    x= x + 1
    print(x)

#method 2 -correct one
x = int(input("enter first number"))
y = x + 5
while x < y :
    x= x + 1
    print(x)

#method 3
x = int(input("enter first number"))
while True:
    x=x+1
    if x == y:
        break
    print(x)