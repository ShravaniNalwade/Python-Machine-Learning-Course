def min(lst,n):
    min=lst[0]
    for i in range(n):
        if(min>lst[i]):
            min=lst[i]
    return min

def main():
    n=int(input("Enter numbers you want in list:"))
    lst=[]
    for i in range(n):
        val=int(input())
        lst.append(val)
    print("List:",lst)
    print("Minimum number is",min(lst,n))


if __name__ =="__main__":
    main()