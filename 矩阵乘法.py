def kkk():
    a=int(input())
    b=int(input())
    c=int(input())
    x=[]
    y=[]
    s=[[0 for i in range(c)]for j in range(a)]
    for i in range(a):
        x.append(list(map(int,input().split())))
    for i in range(b):
        y.append(list(map(int,input().split())))
    for i in range(a):
        for j in range(c):
            for k in range(b):
                s[i][j]+=x[i][k]*y[k][j]
    for i in range(len(s)):
        print(" ".join(list(map(str,s[i]))))


kkk()



