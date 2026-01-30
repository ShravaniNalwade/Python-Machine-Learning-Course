def add(lst,n):
    sum=0
    for i in range(n):
        sum=sum+lst[i]
    return sum

def main():
    n=int(input("Enter numbers you want in list:"))
    lst=[]
    for i in range(n):
        val=int(input())
        lst.append(val)
    print("List:",lst)
    print("Sum is ",add(lst,n))


if __name__ =="__main__":
    main()