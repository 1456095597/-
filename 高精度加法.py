def kkk():
    a=list(input())
    b=list(input())
    x=[]
    y=[]
    c=[]
    t=0
    z=0
    if a[0]=="-" and b[0].isdigit():
        a.pop(0)
        x=b
        y=a
        t=1
    elif a[0]=="-" and b[0]=="-":
        a.pop(0)
        b.pop(0)
        x=a
        y=b
        z=1
    elif b[0]=="-" and a[0].isdigit():
        b.pop(0)
        x=a
        y=b
        t=1
    else:
        x=a
        y=b
    x.remove(" ")
    
    x=list(map(int,x))
    y=list(map(int,y))
    while len(x)<len(y):
        x.insert(0,0)
    while len(y)<len(x):
        y.insert(0,0)
    tag=0
    if t==0:
        i=len(x)-1
        while i>=0:
            x1=x[i]+y[i]
            c.append((x1+tag)%10)
            if x1+tag>=10:tag=1
            else:tag=0
            i-=1
        if tag==1:
            c.append(1)
    zz=0
    zzz=[]
    if t==1:
        for i in range(len(x)):
            if x[i]>y[i]:break
            elif x[i]<y[i]:
                zz=1
                break
        if zz==1:
            zzz=y
            y=x
            x=zzz
            z=1
        i=len(x)-1
        while i>=0:
            if x[i]>=y[i]+tag:
                c.append(x[i]-y[i]-tag)
                tag=0
            else:
                c.append(10+x[i]-y[i]-tag)
                tag=1
            i-=1
    c.reverse()
    c=list(map(str,c))
    if z==1:c.insert(0,"-")
    print("".join(c))


    

kkk()