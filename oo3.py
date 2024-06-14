import sys
class Student(object):
    def __init__(self,code,name,score):
        self.code=code
        self.name=name
        self.score=score
        
if __name__=="__main__":
    objs=[]
    while True:
        print('Welcome ABC edTech\n\n1.Enter Student details\n2.Display Min Score\n3.Exit')
        choice=int(input("\n Enter Your Choice : \n"))
        if choice==1:
            id=int(input("Enter code : "))
            name=input("Enter Name: ")
            score=int(input("Enter Score : "))
            obj=Student(id,name,score)
            objs.append(obj)
        elif choice==2:
            if objs==[]:
                print("----------------------\nNo students details are there\n----------------------")
            min_value=sys.maxsize
            scores=[i.score for i in objs]
            print("\n-------------------------------\nMinimum Value is ",min(scores),"\n---------------------------------")
        elif choice==3:
            sys.exit("\n")
        else:
            pass
