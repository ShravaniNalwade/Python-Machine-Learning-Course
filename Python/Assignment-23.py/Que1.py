class BookStore:
    NoOfBooks=0

    def __init__(self,name,author):
        self.Name=name
        self.Author=author
        BookStore.NoOfBooks=BookStore.NoOfBooks+1

    def Display(self):
        print(f"{self.Name} by {self.Author}.No of Books: {BookStore.NoOfBooks}")

def main():
    name=input("Enter name of Book:")
    author=input("Enter author of Book:")

    obj1=BookStore(name,author)
    obj1.Display()

    name=input("Enter name of Book:")
    author=input("Enter author of Book:")

    obj2=BookStore(name,author)
    obj2.Display()


if __name__ =="__main__":
    main()