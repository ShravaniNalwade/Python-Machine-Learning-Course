def digitSum(Num):
    sum=0
    for i in Num:
        sum=sum+int(i)
    return sum

def main():
    Val=input("Enter Value:")
    print("Sum of digits are ",digitSum(Val))

if __name__ =="__main__":
    main()