def Display(n):
    for i in range(n):  #row
        for j in range(n):
            print("*",end="  ")
        print()
        n=n-1
    

def main():
    No=int(input("Enter No:"))
    Display(No)

if __name__ =="__main__":
    main()