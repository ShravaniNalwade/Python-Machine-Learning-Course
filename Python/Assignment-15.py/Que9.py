from functools import reduce

def main():
    n=(int(input("Enter How many no.s you want:")))
    lst=[]
    print("Enter Numbers")
    for i in range(n):
        val=int(input())
        lst.append(val)
    print("List:",lst)

    print("Product of all elements:",reduce(lambda x,y:x*y, lst))

if __name__ =='__main__':
    main()