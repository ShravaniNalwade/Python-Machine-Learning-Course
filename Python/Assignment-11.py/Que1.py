def prime(No):
    for i in range(2,No):
        if No%i==0:
            return True

    return False

def main():
    Val=int(input("Enter Value:"))
    if (prime(Val)==True):
        print("It is not prime number")
    else:
        print("it is prime number")

if __name__ == "__main__":
    main()