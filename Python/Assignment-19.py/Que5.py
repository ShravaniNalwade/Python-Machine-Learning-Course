from functools import reduce

def main():
    n=int(input("how many numbers you want in list:"))
    lst=[]
    for i in range(n):
        val=int(input())
        lst.append(val)
    print("List:",lst)

    print("List after filter")
    filterLst=list(filter( lambda x:x>1 and all(x%i!=0 for i in range(2,x)) , lst))
    print(filterLst)

    print("List after map")
    mapLst=list(map( lambda x:x*2, filterLst))
    print(mapLst)

    print("after applying reduce ")
    res=reduce( lambda x,y:x if x>y else y , mapLst)
    print(res)

if __name__=="__main__":
    main()  