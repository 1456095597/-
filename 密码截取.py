def kkk():
    a=list(input())
    s=0
    max1=0
    t=0
    for i in range(len(a)-1):
        m=i-1
        n=i+1
        max1=max(s,max1)
        if a[i]==a[i+1]:
            m=i
            s=2
            t=1
        elif a[m]==a[n]:
            s=3
            t=1
        else:
            s=1
            t=0
        while n<len(a)-1 and m>0 and t==1:
            n+=1
            m-=1
            if a[m]==a[n]:
                s+=2
            else:break

    print(max1)

while True:
    try:

        kkk()
    except:
        break