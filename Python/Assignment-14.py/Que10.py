largest=lambda x,y,z: x if(x>y and x>z)  else (y if y>x and y>z else z)

def main():
    No1=int(input("Enter 1st Number:"))
    No2=int(input("Enter 2nd Number:"))
    No3=int(input("Enter 3rd Number:"))
    print("The Largest number is ",largest(No1,No2,No3))

if __name__ =="__main__":
    main()