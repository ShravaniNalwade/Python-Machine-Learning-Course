def Display(n):
    for i in range(1,n+1):  #row
        for j in range(1,i+1):  #column
            print(j,end="  ")
        print()
        
    

def main():
    No=int(input("Enter No:"))
    Display(No)

if __name__ =="__main__":
    main()