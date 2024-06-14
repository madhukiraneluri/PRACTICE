class Bill:
    def __init__(self):
        self.products=[]
        self.totalbill=0
        self.discount=0
    def accept(self):
        n=int(input("Enter no of products : "))
        self.products=[int(input("Enter prod price : ")) for i in range(n)]
    def CalTotal(self):
        self.totalbill=sum(self.products)
        return self.totalbill
    def calDiscount(self):
        if(self.CalTotal()>1000):
            self.discount=10
        self.totalbill-=self.totalbill*self.discount/100
        
obj=Bill()
obj.accept()
print(obj.CalTotal())
obj.calDiscount()
print(obj.totalbill)


    
