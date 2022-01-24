myFile = open("myFile.txt", "r")
print(myFile.read())

myFile.close()


myFile = open("myFile.txt", "r")
#print(myFile.read())

print(myFile.readline())
myFile.close()