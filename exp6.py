def first_two(l):
    if l==[]:
        print("List is Empty ")
        return
    if len(l)<2:
        return l
    temp=l.copy()
    temp.sort()
    return temp[-1],temp[-2]
def last_two(l):
    if len(l)<2:
        return l
    temp=l.copy()
    temp.sort()
    return temp[0],temp[1]


n=int(input("Enter no of students : "))
high=[]
mid=[]
for i in range(n):
    k=int(input())
    if k>=60:
        high.append(k)
    elif k>=40:
        mid.append(k)
max1=first_two(high)
print("Highest Marks : ")
[print(i) for i in max1]
min1=last_two(mid)
print("Lowest Marks : ")
[print(i) for i in min1]
