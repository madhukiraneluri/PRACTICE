import sys
class Account:
    def __init__(self,name,amount):
        self.name=name
        self.pin=1234
        self.amount=amount
        self.passbook=[]
    def deposit(self,val):
        self.amount+=val
        temp=f'Deposit : {val} Remaining Balance : {self.amount}'
        self.passbook.append(temp)
        print("Deposit Completed ")
    def withdraw(self,val):
        if self.amount<val:
            print("Withdrawl amount is higher than the existing")
        else:
            self.amount-=val
            temp=f'Withdrawl : {val} Remaining Balance : {self.amount}'
            self.passbook.append(temp)
            print("Withdrawl completed")
    def balanceEnquiry(self):
        print("Balance : ",self.amount)
    def pinchange(self,old,new):
        if old==self.pin:
            self.pin=new
    def miniStatement(self):
          print("The last 5 transactions are : ")
          temp=self.passbook[::-1]
          for i in temp:
                print(i)
a1=Account("Sherfane Rutherford",40000)
option="yes"
while True and option=="yes": 
    pinNo=int(input("Enter Pin No : "))
    if pinNo==a1.pin:
        print("""
Withdrawl - w
Deposit   - d
Balance Enquiry - b
Pin Change - p
Mini Statement - m
Exit    - e

                """)
        choice=input()
        if choice=="w":
                    val=int(input("Enter Amount to be Withdrawn : "))
                    a1.withdraw(val)
        elif choice=="d":
                    val=int(input("Enter Amount to be deposited : "))
                    a1.deposit(val)
        elif choice == "b":
                    a1.balanceEnquiry()
        elif choice=="p":
                    old=int(input("Enter Old Pin : "))
                    new=int(input("Enter new pin : "))
                    confirm=int(input("confirm the pin once more : "))
                    if new==confirm :
                        if new!=old:
                            a1.pinchange(old,new)
                        else:
                            print("Pin cant be changed dont use the previous pin")
                    else:
                        print("new pin and re entered pin mismatch")
        elif choice=="m":
              print("Hi")
              a1.miniStatement()
        elif choice=="e":
                    sys.exit()
        option=input("Do you want to continue (yes/no) : ")
    else:
        print("Re-Enter pin !! pin is incorrect")


