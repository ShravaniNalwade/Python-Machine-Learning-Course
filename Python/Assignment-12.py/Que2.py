def factors(Num):
    for i in range(1,Num+1):
        if(Num%i==0):
            print(i,end=" ")

def main():
    Val=int(input("Enter Value:"))
    print("Factors are ")
    factors(Val)

if __name__ =="__main__":
    main()