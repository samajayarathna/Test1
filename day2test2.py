#Create a script that increments an integer in a while loop indefinitely. 
# Use an input() method within the loop and, should a user enter 'q', the loop should end

x=0
while True:
    x=x+1
    print(x)
    y=input("enter q to quit")
    if y == 'q':
        break