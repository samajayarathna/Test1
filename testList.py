# Add a method to the class that will display each item in the list using a 'for' loop

class myList():
    def __init__(self, mylist) :
        self.mylist = mylist

    def displayList(self):
        #print(self.mylist)
        for x in self.mylist:
            print(x)


list = ["Apple","Banana","Blueberry","Mango"]

obj1 = myList(list)
obj1.displayList()