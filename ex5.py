def add_bonus(l):
    for i in range(len(l)):
        l[i]+=5000


if __name__=="__main__":
    n=int(input())
    l=[int(input()) for i in range(n)]
    add_bonus(l)
    print(l)
