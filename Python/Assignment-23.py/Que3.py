class Numbers:
    def __init__(self,val):
        self.Value=val
    
    def ChkPrime(self):
        for i in range(2,self.Value):
            if (self.Value % i==0):
                return False
            else:   return True

    def ChkPerfect(self):
        if (self.SumFactors()==self.Value):  return True
        else:   return False

    def Factors(self):
        for i in range(1,self.Value):
            if(self.Value%i == 0):
                print(i,end=" ")
        print()

    def SumFactors(self):
        sum=0
        for i in range(1,self.Value):
            if (self.Value %i ==0):
                sum=sum+i
        return sum

def main():
    no=int(input("Enter Number:"))
    obj1=Numbers(no)

    if (obj1.ChkPrime()): print("It is prime Number")
    else: print("It is Not prime Number")

    if (obj1.ChkPerfect()): print("It is Perfect Number")
    else: print("It is Not Perfect Number")

    print("Factors of given number is:")
    obj1.Factors()

    print("Sum of all factors are ",obj1.SumFactors())



if __name__ =="__main__":
    main()