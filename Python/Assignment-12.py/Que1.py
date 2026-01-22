def check(val):
    if (val=="a" or val=="e" or val=="i" or val=="o" or val=="u"):
        return True
    return False


def main():
    char=input("Enter a Character:")
    if (check(char)):
        print("It is vowel")
    else:
        print("It is Consonant")

if __name__ =="__main__":
    main()