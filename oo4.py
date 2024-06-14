import sys


class Event:
    count=0
    def __init__(self,name,city):
        self.name=name
        self.city=city
        Event.count+=1
if __name__=="__main__":
    while True:
        print("-------------------------------\n1.Regiater Applicant  2.CountApplications 3.Exit\n----------------------------------")
        choice=int(input("Enter choice : "))
        if choice==1:
            name=input("\n Enter Name : ")
            city=input("\nEnter City : ")
            obj=Event(name,city)
        elif choice==2:
            print("No of applicants registered for event is ",Event.count)
        elif choice ==3 :
            sys.exit()
        else:
            pass
