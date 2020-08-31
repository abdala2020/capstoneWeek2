#create a class caled Author
class Author:
    def __init__(self, name):
        self.name = name
        self.books = []
    
    def publish(self,title):
        title = title.lower()
        #handle for duplicate books
        if title in self.books:
            print('Sorry, this book is already in the List of published books')
        else:
            self.books.append(title)

    def __str__(self): 
        # handle for authors with no published books
        if self.books:
            list_of_books = ', '.join(self.books)
            return f'Author name: {self.name}, Books Published : {list_of_books} '
        else:
            return f'Author name: {self.name}, Books Published : No Books'


def main():
    albert = Author('Albert Einstien')
    albert.publish("Science")
    albert.publish("Math")
    albert.publish('math') # this should print an error msg
    print(albert)

    abdala = Author('Abdala Matan')
    print(abdala)

main()

