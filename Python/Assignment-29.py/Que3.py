import sys

def main():
    #Copying Data From old File(Hello.txt)
    oldFile=sys.argv[1]
    oobj=open(oldFile,"r")
    oData=oobj.read()
    oobj.close()

    #Writing Old file contents into new file(Hello.txt -> Demo.txt)
    newFile=input("Enter File Name:")
    nobj=open(newFile,"w")
    print(f"File {newFile} is Opened!")
    nobj.write(oData)
    nobj.close()

    #Reading printing data on console from new file(Demo.txt)
    fobj=open(newFile,"r")
    Data=fobj.read()
    print("New File Contents are:",Data)
    fobj.close()
    print(f"File {newFile} is Closed!")



if __name__ =="__main__":
    main()