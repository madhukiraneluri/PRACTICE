def print_freq(d,val):
    return [i for i in d if d[i]>val]
l=list(map(int,input().split()))
val=int(input("Enter Num to extract elements with frequency greater than your choice : "))

d={i:l.count(i) for i in l}
print(f'Elements greater than frequency {val} are {print_freq(d,val)}')