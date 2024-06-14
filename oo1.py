class Employee:
    gross=0
    def accept(self):
        self.Ecode=int(input("Enter employee code : "))
        self.Ename=input("Enter Employee Name : ")
        self.Msal=int(input("Enter Monthly Salary : "))
    def CalcSal(self):
        self.gross=self.Msal*12
        print(f"Gross salary is {self.gross}")
    def __repr__(self):
        s="Employee Details \n"
        s+=f'Employee code : {self.Ecode}\nEmployee Name : {self.Ename}\nMonthly Salary : {self.Msal}\nGross Salary : {self.gross}'
        return s
emp1=Employee()
emp1.accept()
emp1.CalcSal()
print(emp1)
