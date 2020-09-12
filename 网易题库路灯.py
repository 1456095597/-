def kkk():
    a=list(map(int,input().split()))
    n=a[0]
    l=a[1]
    b=list(map(int,input().split()))
    b.sort()
    i=0
    kk=0
    while i<len(b)-1:
        if b[i+1]-b[i]>kk:
            kk=b[i+1]-b[i]
        i+=1
    kk=kk/2
    if b[0]-n>kk:
        kk=b[0]-n
    if l-b[len(b)-1]>kk:
        kk=l-b[len(b)-1]
    print("%.2f"%(kk))

while True:
    try:
        kkk()
    except:
        break