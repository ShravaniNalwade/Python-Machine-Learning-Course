import os

def main():
    Filename=input("Enter Filename:")
    
    Ret=os.path.exists(Filename)
    if Ret==True:
        print("File is Present")

        fobj=open(Filename,"r")
        # Data=fobj.read()

        print("File Contents")
        cnt=0
        for line in fobj:
            print(line)

    else:
        print("File is not present")

if __name__ =="__main__":
    main()