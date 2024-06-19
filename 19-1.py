class Human:
    def talk(self):
        print("I ........... ")
class Duck:
    def talk(self):
        print("Quak Quak")
class Dog:
    def bark(self):
        print("Bow Bow")
def method(obj):
    if hasattr(obj,"talk"):
        obj.talk()
    elif hasattr(obj,"bark"):
        obj.bark()
    else:
        print("Invalid object")
h=Human()
d=Duck()
do=Dog()
print(list(map(method,[h,d,do])))