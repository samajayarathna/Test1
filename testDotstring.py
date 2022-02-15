class Book():
    """ A class to display a book title and its author
    .....

    Attributes
    ----------

    title : str
        title of a book
    author : str
        author of the book

    Methods
    -------
    display():
        displays the title and the author
    """ 
    def __init__(self, title, author):
        """ initialises the attributes of the class 
        
        Parameters
        ----------
            title : str
                title of a book
            author : str
                author of the book 
        """
        self.title = title
        self.author = author

    def display(self):
        """
        Displays book title and author of book
        
        Parameters
        ----------
            None

        Returns
        -------
        None
        """
        print(self.title, self.author)

x = Book("myTitle", "myAuthor")
x.display()

print(Book.__doc__)  #prints class docstring
print(x.__init__.__doc__) #prints initaliser function docstring
print(x.display.__doc__) #prints display function docstring
