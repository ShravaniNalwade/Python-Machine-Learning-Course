def DigitCheck(num):
    sum=0
    for i in num:
        sum=sum+int(i)
    return sum

def main():
    No=input("Enter No:")
    print(f"Number of digits in {No} are ",DigitCheck(No))

if __name__ =="__main__":
    main()