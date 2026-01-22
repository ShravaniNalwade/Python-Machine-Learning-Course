def reverse(Num):
    res=""
    for i in Num:
        res=i+res
    return res

def main():
    Val=input("Enter Value:")
    reVal=reverse(Val)
    if (Val==reVal):
        print("palindrome")
    else:
        print("Not a Palindrome")

if __name__ =="__main__":
    main()