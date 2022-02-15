# Add a method to the class that will display each item in the list using a 'for' loop
# Add a method to the class that will display each key:value pair in the dictionary using a 'for' loop


class myDictionary():
    def __init__(self, myDic) :
        self.myDic = myDic
    
    def displayDic(self):
        #print(self.myDic)
        # for x, y in self.myDic.items():
        #     print(x,":" ,y)
        for x in self.myDic:
            print(x,":" ,self.myDic[x])

DicValues = {
  "Name": "Sama",
  "Age": 33,
  "year": 1988
}

obj1 = myDictionary(DicValues)
obj1.displayDic()