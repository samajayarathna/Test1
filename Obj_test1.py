class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        
    def display(self):
        print("title is : " + self.title ,"\n author is : " + self.author)
        print(self.title, self.author)

c1 = Book("mybook", "myAuthor")
c1.display()