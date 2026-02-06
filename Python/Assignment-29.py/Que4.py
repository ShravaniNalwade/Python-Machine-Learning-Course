import sys
import os

def main():
    file1=sys.argv[1]
    file2=sys.argv[2]

    Ret1=os.path.exists(file1)
    Ret2=os.path.exists(file2)

    if Ret1==True and Ret2==True :
        print("Both Files are present")

        f1obj=open(file1,"r")
        f2obj=open(file2,"r")
        Data1=f1obj.read()
        Data2=f2obj.read()

        if Data1==Data2:
            print("Sucesss")
        else:
            print("Failure")

        f1obj.close()
        f2obj.close()
    else:
        print("Files are not present")

        

if __name__ =="__main__":
    main()