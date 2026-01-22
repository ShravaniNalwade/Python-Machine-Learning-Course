def add(no1,no2):
    return no1+no2

def sub(no1,no2):
    return no1-no2

def mult(no1,no2):
    return no1*no2

def div(no1,no2):
    return no1/no2

def main():
    Val1=int(input("Enter 1st Value:"))
    Val2=int(input("Enter 2nd Value:"))
    print("Addition is ",add(Val1,Val2))
    print("Subtraction is ",sub(Val1,Val2))
    print("Multiplication is ",mult(Val1,Val2))
    print("Divison is ",div(Val1,Val2))
    
if __name__ =="__main__":
    main()