max=lambda x,y:x if x>y else y

def main():
    No1=int(input("Enter 1st Number:"))
    No2=int(input("Enter 2nd Number:"))
    print("Maximum number is ",max(No1,No2))

if __name__ =="__main__":
    main()