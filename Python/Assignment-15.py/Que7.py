def main():
    n=int(input("Enter How many Strings you want:"))
    lst=[]
    print("Enter String")
    for i in range(n):
        val=input()
        lst.append(val)
    print("List:",lst)

    print("List of Strings having length greater than 5")
    print(list(filter(lambda x:len(x)>5 , lst)))

if __name__ =='__main__':
    main()