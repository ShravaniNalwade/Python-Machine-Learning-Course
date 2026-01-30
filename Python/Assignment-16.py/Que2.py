def ChkNum(No):
    print("Even NUmber") if(No%2==0) else print("Odd Number") 

def main():
    n=int(input("Enter Number:"))
    ChkNum(n)

if __name__ =="__main__":
    main()