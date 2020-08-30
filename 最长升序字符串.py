def kkk():
    a=input()
    a=list(map(int,input().split()))
    d=[]
    x=0
    xx=0
    for i in range(len(a)):
        if i==0:d.append(1)
        else:
            x=1
            for j in range(i):
                if a[i]>a[j]:
                    x=max(x,d[j]+1)
            d.append(x)
        xx=max(d[i],xx)
    print(xx)


kkk()
    
        
