def mp3f():
    b=int(input())
    a=[]
    x1=0
    x2=3
    x=0
    for i in range(b):
        a.append(i+1)
    l1=list(input())
    for i in range(len(l1)):
        if l1[i]=="U":
            if x==0:
                x=len(a)-1
                x2=len(a)-1
                x1=len(a)-4
            elif x==x1:
                x=x-1
                x1=x1-1
                x2=x2-1
            else:x=x-1
        else:
            if x==len(a)-1:
                x=0
                x1=0
                x2=3
            elif x==x2:
                x=x+1
                x1=x1+1
                x2=x2+1
            else:x=x+1
    print(" ".join(list(map(str,a[x1:x2+1]))))
    print(x1)
    print(x2)
    print(a[x])


mp3f()




