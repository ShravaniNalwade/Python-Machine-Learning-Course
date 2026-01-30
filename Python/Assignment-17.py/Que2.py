def Display(n):
    for i in range(n):
        for j in range(n):
            print("*",end="  ")
        print()
    

def main():
    No=int(input("Enter No:"))
    Display(No)

if __name__ =="__main__":
    main()