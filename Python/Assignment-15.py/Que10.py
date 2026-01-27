def main():
    n=int(input("Enter How many Numbers you want:"))
    lst=[]
    print("Enter Number")
    for i in range(n):
        val=int(input())
        lst.append(val)
    print("List:",lst)

    print("List of Even Numbers")
    print(list(filter(lambda x:x%2==0  , lst)))

if __name__ =='__main__':
    main()