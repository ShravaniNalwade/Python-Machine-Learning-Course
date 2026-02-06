import os

def main():
    Filename=input("Enter Filename:")
    
    Ret=os.path.exists(Filename)
    if Ret==True:
        print("File is Present")

        fobj=open(Filename,"r")
        Data=fobj.read()

        cnt=0
        for word in Data.split():
            cnt=cnt+1

        print("Total words are ",cnt)

    else:
        print("File is not present")

if __name__ =="__main__":
    main()