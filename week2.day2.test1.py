#Set ‘total’ to zero 
# Set ‘counter’ to zero 
# While counter is less than 5 
#   Get number
#   add number to total 
#   increment counter 
#Calculate the average of the total 
# Display the average

total = 0 
counter = 0 

while counter < 5: 
    number = int(input("enter first number: ")) 
    total = total + number 
    counter = counter + 1 
    average = total / 5 
    print("the average is: ", average)