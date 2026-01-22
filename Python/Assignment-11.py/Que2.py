def count(Num):
    cnt=0
    for i in Num:
        cnt=cnt+1
    return cnt

def main():
    Val=input("Enter Value:")
    print("Count of digits are ",count(Val))

if __name__ =="__main__":
    main()