import os

def main():
    Filename=input("Enter Filename:")
    
    Ret=os.path.exists(Filename)
    if Ret==True:
        print("File is Present")

        fobj=open(Filename,"r")
        # Data=fobj.read()

        #File object is iterable(line-by-line)
        cnt=0
        for line in fobj:
            cnt=cnt+1

        print("Total Lines are ",cnt)

    else:
        print("File is not present")

if __name__ =="__main__":
    main()