#Define a function that accepts a number parameter and prints it. Call the function from the script

def my_function(number1):
    print(number1)

my_function(5)

#Create a script that asks for two numbers inputted from the command line, passes those two numbers 
# as arguments to a function. The function will add the two numbers, and return the result to be printed 
# from the main part of the script.


a= int(input("Enter first number  "))
b= int(input("Enter second number  "))

def add_function(num1,num2):
    sum = num1 + num2
    return sum 
    
print(add_function(a,b))

#write a script that uses a function with a local variable. Add that local variable
# to a passed value and display the result. 
#Use the same variable name in the body of the script, assign it a value
#  and pass it to the function

#myone
x = "sama"

def local_variable (x):
    x="string"
    print(x)

#
def myfunc(z):
    num =9
    print(z+9)

num =7
myfunc(num)


local_variable(x)