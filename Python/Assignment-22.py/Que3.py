class Arithmetic:

    def __init__ (self):
        self.Value1=0
        self.Value2=0

    def Accept(self,a,b):
        self.Value1=a
        self.Value2=b

    def Addition(self):
        return self.Value1 + self.Value2

    def Substraction(self):
        return self.Value1 - self.Value2

    def Multiplication(self):
        return self.Value1 * self.Value2

    def Division(self):
        try:
            return self.Value1 / self.Value2

        except:
            return "Not defined"

def main():
    obj1=Arithmetic()
    obj2=Arithmetic()

    # no1=int(input("Enter 1st number:"))
    # no2=int(input("Enter 2nd number:"))

    obj1.Accept(10,20)
    print("Addition is:",obj1.Addition())
    print("Substraction is:",obj1.Substraction())
    print("Multiplication is:",obj1.Multiplication())
    print("Division is:",obj1.Division())
    print()
    
    obj2.Accept(-10,0)
    print("Addition is:",obj2.Addition())
    print("Substraction is:",obj2.Substraction())
    print("Multiplication is:",obj2.Multiplication())
    print("Division is:",obj2.Division())

if __name__ =="__main__":
    main()