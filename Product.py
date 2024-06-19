class Product:
    count=0
    netAmount=0
    def __init__(self,name,price,units):
        self.name=name
        self.price=price
        self.units=units
        Product.netAmount+=self.price*self.units
    def __repr__(self) -> str:
        Product.count+=1
        res=f"********Product {Product.count} ********"
        res+=f"\nName : {self.name}\nUnits : {self.units}\n Price:{self.price}"
        res+=f"\n=========={Product.netAmount}======="
        return res
n=int(input("Enter no of products to store : "))
objs=[]
for i in range(n):
    print("Enter Details for Product {}".format(i+1))
    name=input("Enter Product Name : ")
    price=int(input("Enter Price : "))
    units=int(input("Enter no of units : "))
    obj=Product(name,price,units)
    objs.append(obj)
for i in objs:
    print(i)