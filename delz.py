def delz():
    a=list(input())
    b=999
    c=[]
    for i in range(len(a)):
        if a.count(a[i])<b:
            c.clear()
            c.append(a[i])
            b=a.count(a[i])
        elif a.count(a[i])==b :
            if c.count(a[i])==0:
                c.append(a[i])
    for i in range(len(c)):
        a.remove(c[i])
    print("".join(a))


delz()
    

