def Display(n):
    for i in range(1,n+1):  #rows
        for j in range(1,n+1):  #columns
            print(j,end="  ")
        print()
    

def main():
    No=int(input("Enter No:"))
    Display(No)

if __name__ =="__main__":
    main()