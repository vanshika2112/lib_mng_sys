class library:
    books = []
    lib_name=""
    d = {}
    def __init__(self, x,y):
        books = x
        lib_name = y

    def display(self):
        print(f"--{self.lib_name}--")
        for x in self.books:
            print(x)

    def addf(self,z):
        self.books.append(z)

    def lend(self,x, y):
        if x in self.d:
            print("Not Available")
        else:
            self.d[x]=y

    def returnb(self,x):
        self.d.pop(x)

    def disp(self):
        print(self.d)

x = input("Type library name  ")
l=[]
obj = library(l,x)
library.lib_name=x
while 1 :
    print(" 1 - To display library")
    print(" 2 - To lend a book")
    print(" 3 - To Add a book")
    print(" 4 - To Return a book")
    print(" 5 - To display books borrowed by students")
    print("")
    ch = int(input("Choose the above options  "))
    print("")
    if ch==1:
        obj.display()
    elif ch==2:
        x = input("Book you want  ")
        y = input("Your name  ")
        obj.lend(x,y)
    elif ch==3:
        x = input("Book name  ")
        obj.addf(x)
    elif ch==4:
        x = input("Book name  ")
        obj.returnb(x)
    elif ch==5:
        obj.disp()
    else:
        break;
    print("")
    print("Done, Next->  ")
    print("")
