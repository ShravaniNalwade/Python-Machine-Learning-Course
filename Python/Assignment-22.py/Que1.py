class Demo:
    Value=10        #Class Variable

    def __init__(self,a,b):
        print("--Inside Constructor--")
        self.no1=a      #Instance Variables
        self.no2=b       #Instance Variables

    def Fun(self):
        print("--Inside Fun--")
        print("Value of no1 and no2 are ",self.no1,self.no2)

    def Gun(self):
        print("--Inside Gun--")
        print("Value of no1 and no2 are ",self.no1,self.no2)

def main():
    obj1=Demo(11,21)
    obj2=Demo(51,101)

    obj1.Fun()
    obj2.Fun()
    obj1.Gun()
    obj2.Gun()

if __name__ =="__main__":
    main()


    

        
