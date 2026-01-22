def fact(No):
    if No==0:
        return 1
    elif No<0:
        return "Undefined"
    else:
        mult=1
        for i in range(1,No+1):
            mult=mult*i
        return mult


def main():
    Val=int(input("Enter Value:"))
    print("Factorial is:",fact(Val))

if __name__ == "__main__":
    main()