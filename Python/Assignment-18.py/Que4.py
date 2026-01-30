def Freqency(lst,n,val):
    freq=0
    for i in range(n):
        if(val==lst[i]):
            freq=freq+1
    return freq

def main():
    n=int(input("Enter numbers you want in list:"))
    lst=[]
    for i in range(n):
        val=int(input())
        lst.append(val)
    print("List:",lst)
    val=int(input("Enter Value to check its frequency:"))
    print("Frequency is ",Freqency(lst,n,val))


if __name__ =="__main__":
    main()