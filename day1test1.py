#Create a script using an inner and outer for loop. The inner loop loops through the letters of the alphabet, 
# and the outer loop loops through numbers 0 – 10. Print once each iteration through the inner loop and once
#  for each iteration through the outer loop.

myString = "abcdefg"
myNumbers = "123"

for x in myNumbers:
    print(x[0])
    for y in myString:
        print(y[0])
        

i =0
j= 0

for x in myNumbers:
    print(myNumbers[i]);
    for y in myString:
        print(myString[j])
        j=j=1

i=i+1
j=0

for every