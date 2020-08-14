def kkk():
    a=list(input().split())
    b=list(input().split())
    a.pop(0)
    b.pop(0)
    b=list(set(b))
    b=list(map(int,b))
    b.sort()
    b=list(map(str,b))
    print(b)
    c=[]
    for i in range(len(b)):
        c.append(b[i])
        x=0
        xx=len(c)
        for j in range(len(a)):
            if b[i] in a[j]:
                x+=1
                c.append(str(j))
                c.append(a[j])
       
        c.insert(xx,x)
        if x==0:
            c.pop()
            c.pop()
    c.insert(0,str(len(c)))
    print(" ".join(list(map(str,c))))


kkk()
