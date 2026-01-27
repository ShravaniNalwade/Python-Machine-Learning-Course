def main():
    n=(int(input("Enter How many no.s you want:")))
    lst=[]
    print("Enter Numbers")
    for i in range(n):
        val=int(input())
        lst.append(val)
    print("List:",lst)
    print("List of Even Numbers:",list(filter(lambda x:(x%2==0), lst)))

if __name__ =='__main__':
    main()