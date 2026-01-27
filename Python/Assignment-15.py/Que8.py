def main():
    n=int(input("Enter How many Numbers you want:"))
    lst=[]
    print("Enter Number")
    for i in range(n):
        val=int(input())
        lst.append(val)
    print("List:",lst)

    print("List of Numbes divisible by 3 and 5")
    print(list(filter(lambda x: x%3==0 and x%5==0 , lst)))

if __name__ =='__main__':
    main()