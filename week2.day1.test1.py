#write a script that divides an integer by zero. Use a catch all exception to catch the error and print a relative 
# warning message

try:
    num1 = int(input("Enter a number "))
    num2 = int(input("Enter a number "))
    z = num1/num2

except ValueError:
    print("only numbers are valid")
except ZeroDivisionError:
    print("cannot divide by zero")

#write a script that attempts to concatenate a string with an integer. Use catch all try/except statement to catch
#  the error and print a warning message


try:
    print("test" + 5)
    str1 = input("enter your name")

except Exception:
    print("cannot join string to integer")


