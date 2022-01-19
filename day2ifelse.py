
#display whether the variables are the same or different. 
a= "john"
b= "Sam"

if a == b:
    print("strings are equal")
else:
    print("strings are not equal")

num1= input("Enter first number ")
num2 = input("Enter second number ")

if( num1 > num2):
    print(num1 ,"is greater than ",num2)
elif( num1 == num2):
    print(num1, "and" ,num2 , "are same")
else:
    print(num1, "is smaller than", num2)