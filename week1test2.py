#create a string variable that holds the numbers 0 to 9; Use a for loop to iterate over the string and print it out

a = "0123456789"
for everyElement in a:
    print(everyElement)

print(list(range(0,9)))

#Create two for loops, inner and outer. The outer loop should display the values 0 to 9
# The inner loop should display the values 9 to 0

for everyNumber in range(0,3):
    print(everyNumber)
    for everyNumber in reversed(range(10,0)):
        print(everyNumber)

#anotherway
for b in range(0,3):
    print(b)
    for i in range(3,0,-1):
        print(i)

