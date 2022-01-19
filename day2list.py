list1 = ["banana", "apple" ,"cherry"]
print(list1) # display list items

#Use count() and display the number of items of a particular value in the list
list2 =["a","b","a"] 
print(list2.count("a"))

#display second item in the list
list3 = ["a","b","c"]
print(list3[2])

#Use indexing to change the value of the third item
list3[2] = "d"
print(list3)

#Use append() to add an item to the list and then display to confirm the change
list3.append("c")
print(list3)