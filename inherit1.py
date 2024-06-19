class Employee:
    role=None
    dept=None
    sal=0
    def __init__(self,role,dept,sal):
        self.role=role
        self.dept=dept
        self.sal=sal

    def showDetails(self):
        print(self.dept,self.role,self.sal)
class Engineer(Employee):
    def __init__(self,name,age,role,dept,sal):
        super().__init__(role,dept,sal)
        self.name=name
        self.age=age
    def showDetails(self):
        print(self.name,self.age)
        super().showDetails()
obj=Engineer("madhu",22,"Engineer","Software",20000)
obj.showDetails()