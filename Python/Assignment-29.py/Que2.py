import os

def main():
    try:
        Filename=input("Enter Filename:")
        Ret=os.path.exists(Filename)
        if Ret==True:
            print("File is present")
        else:
            print("File is not present")

        fobj=open(Filename,"w")
        Data=input("Enter File Contents:")
        fobj.write(Data)
        fobj.close()

        fobj=open(Filename,"r")
        rdata=fobj.read()
        print("Contents of File are:",rdata)

        fobj.close()
        print("File get Closed")
    
    finally:
        print("End")

if __name__ =="__main__":
    main()