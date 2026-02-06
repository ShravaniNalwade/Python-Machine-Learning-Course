import os

def main():
    Filename=input("Enter Filename:")
    fobj=open(Filename,"r")
    fdata=fobj.read()
    fobj.close()

    string=input("Enter String:")
    frq=0
    for s in fdata.split(): #splits Line into words so words will be itrate not letters
        if  s==string:
            frq=frq+1

    print("Total Frequency is ",frq)

if __name__ =="__main__":
    main()