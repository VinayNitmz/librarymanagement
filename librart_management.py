class Library:

    def __init__(self, list_of_book , library_name):
        self.list_of_book = list_of_book
        self.library_name = library_name
        self.book_dict = {}

    def display(self):

        print(self.list_of_book)

    def lendbook(self, book, user):
        if book not in self.book_dict.keys():
            self.book_dict.update({book:user})
            self.list_of_book.remove(book)
            print("Book issued")
        else:
            print("Book already been issued by", self.book_dict[book])


    def addbook(self):
        abook = input("Enter book you want to add\n")
        self.list_of_book.append(abook)
        print("book has been added ")

    def returnbook(self):
        rbook = input("Enter book name to be returned\n")
        if rbook not in self.book_dict:
            print("You have entered invalid book name kindly try again")
            vinay.returnbook()
        else:
            self.book_dict.pop(rbook)
            self.list_of_book.append(rbook)
            print("Returned successfully")

if __name__ == '__main__':

    list_of_book = ["aaaa", "bbbb", "cccc", "dddd", "eeee"]
    library_name = 'vinay library'

    vinay = Library(list_of_book,library_name)

    while(True):

        print(f"Welcome to {vinay.library_name}.\n press 1 to display book \n press 2 to lend book \n press 3 to add book \n press 4 to return book")
        user_input = int(input())

        if user_input == 1:
            vinay.display()

        elif user_input == 2:
            book = input("Enter book to be issued\n")
            user = input("Enter your name\n")
            vinay.lendbook(book,user)

        elif user_input == 3:
            vinay.addbook()

        elif user_input == 4:
            vinay.returnbook()

        else:
            print("enter valid input")

        user_input2 = input("q to quit else c to continue\n")

        if user_input2 == 'q':
            exit()
        else:
            continue


