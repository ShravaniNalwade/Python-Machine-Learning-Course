def FactSum(n):
    sum=0
    for i in range(1,n):
        if(n%i==0):
            sum=sum+i
    return sum

def main():
    No=int(input("Enter No:"))
    print("Sum of factors",FactSum(No))

if __name__ =="__main__":
    main()