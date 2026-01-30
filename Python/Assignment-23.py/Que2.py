class BankAccount:
    ROI=10.5

    def __init__(self,name,amt):
        self.Name=name
        self.Amount=amt

    def Display(self):
        print(f"Account Holder Name:{self.Name}")
        print(f"Currunt Balance:{self.Amount}")

    def Deposit(self,depo):
        self.Amount=self.Amount + depo

    def Withdraw(self,withdrawamt):
        if (withdrawamt<=self.Amount):
            self.Amount=self.Amount - withdrawamt
        else:   print("Balance is not sufficient")

    def CalculateInterest(self):
        self.Interest = (self.Amount * BankAccount.ROI)/100
        return self.Interest

def main():
    name=input("Enter your Name:")
    amt=int(input("Enter Amount:"))
    obj1=BankAccount(name,amt)
    obj1.Display()
    depo=int(input("Enter Amount for Deposite:"))
    obj1.Deposit(depo)
    obj1.Display()
    withdrawamt=int(input("Enter Amount for withdrawal:"))
    obj1.Withdraw(withdrawamt)
    obj1.Display()
    print("Total Interest on amount is: ",obj1.CalculateInterest())

if __name__ =="__main__":
    main()