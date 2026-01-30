import ModuleArithemetic

def main():
    a=int(input("Enter 1st No:"))
    b=int(input("Enter 2nd No:"))

    print("Addition :",ModuleArithemetic.Add(a,b))
    print("Substraction :",ModuleArithemetic.Sub(a,b))
    print("Multiplication :",ModuleArithemetic.Mult(a,b))
    print("Division :",ModuleArithemetic.Div(a,b))

if __name__ =="__main__":
    main()