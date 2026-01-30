def max(lst,n):
    max=0
    for i in range(n):
        if(max<lst[i]):
            max=lst[i]
    return max

def main():
    n=int(input("Enter numbers you want in list:"))
    lst=[]
    for i in range(n):
        val=int(input())
        lst.append(val)
    print("List:",lst)
    print("Maximum number is",max(lst,n))


if __name__ =="__main__":
    main()