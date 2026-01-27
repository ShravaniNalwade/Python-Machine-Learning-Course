min=lambda x,y:y if x>y else x

def main():
    No1=int(input("Enter 1st Number:"))
    No2=int(input("Enter 2nd Number:"))
    print("Minimum number is ",min(No1,No2))

if __name__ =="__main__":
    main()