def divisible(No1):
    if((No1%3==0) and (No1%5==0)):
        print("Divisible by 3 and 5")
    else:
        print("Number is not Divisible by 3 and 5")


def main():
    Val=int(input("Enter any Number:"))
    divisible(Val)

if __name__ == "__main__":
    main()