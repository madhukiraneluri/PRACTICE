def isDiv(t):
    for i in t:
        if i%2!=0:
            return False
    return True
n=int(input("Enter no of tuples : "))
l=[tuple(map(int,input().split())) for i in range(n)]

print("\nTuples where each element divisible by 2 are : \n")
res=[i for i in l if isDiv(i)]
print(res)
