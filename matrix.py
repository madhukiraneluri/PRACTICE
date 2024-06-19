import numpy as np
n=int(input("Enter no of rows : "))
l=[]
for i in range(n):
    l.append(list(map(int,input().split())))
arr=np.array(l)
row_sum=np.sum(arr,axis=0)
col_sum=np.sum(arr,axis=1)
diagn1=np.trace(arr)
print(row_sum,col_sum,diagn1)