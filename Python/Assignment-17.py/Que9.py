def DigitCheck(num):
    cnt=0
    for i in num:
        cnt=cnt+1
    return cnt

def main():
    No=input("Enter No:")
    print(f"Number of digits in {No} are ",DigitCheck(No))

if __name__ =="__main__":
    main()