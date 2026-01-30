def Prime(n):
    for i in range(2,n):
        if(n%i==0):
            print("It is not prime")
            return
        else:
            print("It is prime")
            return

def main():
    No=int(input("Enter No:"))
    Prime(No)

if __name__ =="__main__":
    main()