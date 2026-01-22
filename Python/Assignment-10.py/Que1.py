def multTable(No):
    print(f"Table of {No} is")
    for i in range(1,11):
        print(No*i,end=" ")

def main():
    Val=int(input("Enter Number:"))
    multTable(Val)

if __name__ == "__main__":
    main()