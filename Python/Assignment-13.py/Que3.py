def checkPerfect(no):
    sum=0
    for i in range(1,no):
        if(no%i ==0):
            sum=sum+i
    if(sum==no):
        return True
    else: return False


def main():
    val=int(input("Enter Number:"))
    if(checkPerfect(val)):
        print("It is Perfect Number")
    else:
        print("It is not a Perfect Number")

if __name__ =="__main__":
    main()