class Circle:
    PI=3.14     #Class Variable
    
    def __init__(self):
        #Instance Variables
        self.Radius=0.0
        self.Area=0.0
        self.Circumference=0.0

    def Accept(self):
        self.Radius=int(input("Enter Radius of Circle:"))
        
    def CalculateArea(self):
        self.Area=Circle.PI* self.Radius* self.Radius
        # return Area

    def CalculateCircumference(self):
        self.Circumference=Circle.PI* self.Radius
        # return Circumference

    def Display(self):
        print("Value of Radius:",self.Radius)
        print("Value of Area:",self.Area)
        print("Value of Circumference:",self.Circumference)

def main():
    obj1=Circle()
    obj1.Accept()
    obj1.CalculateArea()
    obj1.CalculateCircumference()
    obj1.Display()

if __name__=="__main__":
    main()


