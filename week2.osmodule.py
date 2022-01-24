import os
# if os.path.exists('c:/test/test.txt'):
#     print("exists")
# else:
#     print("does not exist")

# Use os.path.exists() and an if statement to determine if a file titled "myFile.txt exists. Print "the file exists"
#  if it does exist. Otherwise print "file does not exist", and create the file using a write() function 
# #Check the file has been created


if os.path.exists('C:/Users/samaj/OneDrive/Documents/GitHub/Test1/myFile.txt'):
    print("the file exists")
else:
    print("file does not exist")

myFile = open("myFile.txt", "w")
myFile.close()
