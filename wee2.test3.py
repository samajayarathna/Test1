#1#Write a script that creates a new file titled "myFile.txt" and writes the string "this has been written" to the file.
#  Open the file with notepad.exe to prove that the string has been written.


myFile = open("myFile.txt", "w")

myFile = open("myFile.txt", "a")
myFile.write("this has been written")
myFile.close()

myFile = open("myFile.txt", "r")
print(myFile.read())

#Write a script that takes in three single strings via three input() methods, writes them to a file with each on
#  a new line, and then reads the file and prints the contents

x = open("myFile.txt", "w")
x.write("line 1")
x.write("\nline 2")
x.write("\nline 3")
x.close()

x = open("myFile.txt", "r")
print(x.read)()