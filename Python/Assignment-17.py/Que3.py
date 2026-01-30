def Factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact

def main():
    No=int(input("Enter No:"))
    print("Factorial:",Factorial(No))

if __name__ =="__main__":
    main()