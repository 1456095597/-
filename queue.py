def queue():
    input()
    a=input().split()
    b=[]
    max1=0
    c=[1]*len(a)
    cc=[1]*len(a)
    for i in range(len(a)):
        b.append(int(a[i]))
    for i in range(len(b)):
        if i!=0:
            for j in range(i):
                if b[j]<b[i]:
                    c[i]=max(c[j]+1,c[i])
    b.reverse()
    for i in range(len(b)):
        if i!=0:
            for j in range(i):
                if b[j]<b[i]:
                    cc[i]=max(c[j]+1,cc[i])
    
    for i in range(len(c)):
        max1=max(c[i]+cc[len(c)-i-1]-1,max1)
    print(len(a)-max1)

queue()
