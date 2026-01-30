from functools import reduce

def main():
    n=int(input("how many numbers you want in list:"))
    lst=[]
    for i in range(n):
        val=int(input())
        lst.append(val)
    print("List:",lst)

    print("List after filter")
    filterLst=list(filter( lambda x:x>=70 and x<=90 , lst))
    print(filterLst)

    print("List after map")
    mapLst=list(map( lambda x:x+10 , filterLst))
    print(mapLst)

    print("after applying reduce ")
    res=reduce( lambda x,y:x*y , mapLst)
    print(res)

if __name__=="__main__":
    main()