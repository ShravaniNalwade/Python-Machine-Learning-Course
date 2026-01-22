def allEven(No):
    for i in range(0,No+1,2):
        print(i,end=" ")

def main():
    Val=int(input("Enter Value:"))
    allEven(Val)

if __name__ =="__main__":
    main()