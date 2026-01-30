import MarvellousNum

def ListPrime(n):
    lst=[]
    for i in range(n):
        val=int(input())
        lst.append(val)
    return MarvellousNum.ChkPrime(n,lst)


def main():
    n=int(input("How many numbers you want in list:"))
    print("Addition of prime numbers in list:",ListPrime(n))

if __name__=="__main__":
    main()