import os

def main():

        Filename=input("Enter File Name:")
        # open(Filename,"w")    If not present then it will Create it
        Ret=os.path.exists(Filename)
        if Ret==True:
            print(f"File {Filename} is Present")
        else:
            print(f"File {Filename} is not  Present")


if __name__ =="__main__":
    main()