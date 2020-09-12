def kkk():
    a=list(map(int,input().split()))
    a.sort()
    s=0
    while a!=[]:
        n=a.count(a[0])
        if n%(a[0]+1)!=0:
            s+=n-(n%(a[0]+1))+a[0]+1
        else:
            s+=n
        x=a[0]
        while a[0]==x:
            a.pop(0)
            if len(a)==0:
                break
    print(s)

while True:
    try:
        kkk()
    except:
        break