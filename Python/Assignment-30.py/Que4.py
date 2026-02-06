import os

def main():
    File1=input("Enter Existing Filename:")
    File2=input("Enter New Filename:")

    
    Ret=os.path.exists(File1)
    if Ret==True:
        print("Existing File is Present")

        #Reading data from existing file
        f1=open(File1,"r")
        data1=f1.read()
        f1.close()

        #Writing Data into new file
        f2=open(File2,"w")
        f2.write(data1)
        f2.close()
        print("Copied contents successfully")
        
        #printing data from new file
        f2=open(File2,"r")
        print("New File contents are:",f2.read())
        f2.close()

        print("Closed both files")

    else:
        print("Existing File is not present")

if __name__ =="__main__":
    main()