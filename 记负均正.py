def kkk():
    x=[]
    n=0
    a=int(input())
    b=list(map(int,input().split()))
    for i in range(a):
        
        if b[i]<0:n+=1
        elif b[i]>0:x.append(b[i])
    s=sum(x)
    print(s)
    x=s/len(x)
    print("%d %.1f"%(n,x))


kkk()
  