def Display(name):
    cnt=0
    for i in name:
        cnt=cnt+1
    return cnt

def main():
    name=input("Enter Name:")
    print(len(name))
    print(Display(name))

if __name__ =="__main__":
    main()

