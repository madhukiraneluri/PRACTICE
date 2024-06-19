class Candidate:
    def __init__(self,name,qual,age):
        self.name=name
        self.qual=qual
        self.age=age
    class Validator:
        def validateAge(my,ref):
            if ref.age>=21 and ref.age<=25:
                print("Acccess Granted")
            else:
                print("Access Not Granted")
    def validate(self):
        obj=self.Validator()
        obj.validateAge(self)
c=Candidate("madhu","btech",22)
c1=Candidate("kiran","Bcom",19)
c.validate()
c1.validate()
            