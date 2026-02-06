import os

def main():
    File=input("Enter Existing Filename:")
    word=input("Enter word:")

    Ret=os.path.exists(File)
    if Ret==True:
        print("Existing File is Present")

        #Reading data from existing file
        f1=open(File,"r")
        data1=f1.read()

        found=False
        for w in data1.split():
            if(w==word):
                found=True
                break  

        if found==True:
            print("Word is present")
        else:
            print("Word is not present")
        f1.close()

    else:
        print("Existing File is not present")

if __name__ =="__main__":
    main()