#Create a script that asks for your name and your age and then displays your name and age plus one year
#Add to the above script using an if statement, so that if the age plus one is equal to 100, a message displays 
# "Congratulations you are going to be 100"
name = input("Enter your name")
age = int(input("Enter your age"))

def display_name(name):
    print("Your name is " ,name)

def display_age(age):
    age_new = age + 1
    print("Your age is after one year ", age_new )
    if age_new == 100:
        print("Congratulations you are going to be 100")

display_name(name) #display name
display_age(age) # display age after one year