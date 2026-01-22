def sumN(No):
    sum=0
    for i in range(1,No+1):
        sum=sum+i
    return sum


def main():
    Val=int(input("Enter Value:"))
    print(sumN(Val))

if __name__ == "__main__":
    main()