#Create a while loop that increments a variable 100 times and displays each value. The loop should then exit

# x= 0
# while x < 101:
#     print(x)
#     x += 1
    
#Create a function that accepts a single integer argument, adds five to it, returns the value to the calling code and, 
# displays it

num1 = int(input("Enter an integer value"))

def display_values(num1):
    add_value = num1 + 5
    print(add_value)

display_values(num1)
