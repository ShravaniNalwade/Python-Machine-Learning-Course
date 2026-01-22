def reverse(Num):
    res=""
    for i in Num:
        res=i+res
    return res

def main():
    Val=input("Enter Value:")
    print("Reverse Number is",reverse(Val))

if __name__ =="__main__":
    main()