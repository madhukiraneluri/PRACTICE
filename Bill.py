class Bill:
    def __init__(self):
        self.products=[]
        self.netbalance=0
    def accept(self):
        n=int(input("Enter no of products to store : "))
        for i in range(n):
            print(f'Enter details for product {i+1}\n--------------------------------')
            d={}
            d['name']=input("Enter product name : ")
            d['price']=int(input("Enter Price : "))
            d['units']=int(input("Enter no of units : "))
            self.products.append(d)
    
    def calNetbal(self):
        for i in self.products:
            self.netbalance+=i['price']*i['units']
    0
    def __repr__(self):
        res=""
        c=1
        for i in self.products:
            res+=f"*******Product{c}*******\n"
            res+=f"Name : {i['name']}\nUnits : {i['units']}\nPrice : {i['price']}\n\n"
            c+=1
        res+=f"===========Net Amount = {self.netbalance} =================="
        return res
obj=Bill()
obj.accept()
obj.calNetbal()
print(obj)