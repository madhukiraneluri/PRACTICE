import sys
class Person:
    def __init__(self,name,age,email):
        self.name=name
        self.age=age
        self.email=email
class Employee(Person):
    def __init__(self, name, age, email,id,dept,role,sal):
        self.id=id
        self.dept=dept
        self.role=role
        self.sal=sal
        super().__init__(name, age, email)
    @property
    def gross(self):
        return self.sal*12
    def __repr__(self):
        res=""
        res+="==============Employee Details===============\n"
        res+="Name : {}\nAge: {}\nEmail: {}\nId: {}\ndept: {}\nrole: {}\nsal: {}\nGross Salary : {}\n".format(self.name,self.age,self.email,self.id,self.dept,self.role,self.sal,self.gross)
        return res
class Student(Person):
    def __init__(self, name, age, email,id,dept,marks):
        self.id=id
        self.dept=dept
        self.marks=marks
        super().__init__(name, age, email)
    @property
    def avg(self):
        return sum(self.marks)/len(self.marks)
    @property
    def grade(self):
        n=self.avg
        if n>=90:
            return 'A'
        elif 80<= n <90:
            return 'B'
        elif 70 <= n <80:
            return 'C'
        elif 60 <= n <70:
            return 'D'
        else:
            return 'F'
    def __repr__(self):
        res=""
        res+="==============Student Details===============\n"
        res+="Name : {}\nAge: {}\nEmail: {}\nId: {}\ndept: {}\navg : {}\nGrade: {}".format(self.name,self.age,self.email,self.id,self.dept,self.avg,self.grade)
        return res
students=[]
employee=[]
persons=[]
while True:
    print("\n\nWhom Details You Want to Enter : ??\n1.Employee\n2.Student\n3.All Employee Details\n4.All Students details\n5.Need person Details based on Age \n6.exit")
    choice=int(input("Enter your choice among 1,2,3,4,5,6 : "))
    if choice==1:
        name=input("Enter name : ")
        age=int(input("Enter Age : "))
        mail=input("Enter email id : ")
        id=int(input("Enter ID : "))
        dept=input("Enter Department : ")
        role=input("Enter Role : ")
        sal=int(input("Enter Salary : "))
        employee.append(Employee(name,age,mail,id,dept,role,sal))
    elif choice==2:
        name=input("Enter name : ")
        age=int(input("Enter Age : "))
        mail=input("Enter email id : ")
        id=int(input("Enter ID : "))
        dept=input("Enter Department : ")
        marks=list(map(int,input("Enter marks of 5 Subjects with a space").split()))
        students.append(Student(name,age,mail,id,dept,marks))
    elif choice==3:
        print("Details of All Existing Employee are : ")
        [print(i) for i in employee]
    elif choice==4:
        print("Details of All Existing Students are : ")
        [print(i) for i in students]
    elif choice==5:
        age=int(input("Enter Which age Persons you need : "))
        [print(i.name,i.age) for i in persons if i.age==age]
    elif choice==6:
        sys.exit()
    persons=students+employee
