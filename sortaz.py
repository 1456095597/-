def sortz():
    a=list(input())
    b=[]
    for i in range(len(a)):
        if (a[i].isalpha()):
            b.append(a[i])
    b = sorted(b, key = str.lower)
    j=0
    for i in range(len(a)):
        if (a[i].isalpha()):
            a[i]=b[j]
            j+=1
    print("".join(a))

def namec():
    a=int(input())
    c=[]
    sum=0
    for i in range(a):
        b=list(input())
        for j in range(len(b)):
            if c.count(b[j])==0:
                c.append(b[j])
        cc=[]
        for j in range(len(c)):
            cc.append((b.count(c[j])))
        cc.sort(reverse=True)
        for j in range(len(cc)):
            sum+=(26-j)*cc[j]
        print(sum)
        sum=0


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
                    cc[i]=max(ccj]+1,cc[i])
    
    for i in range(len(c)):
        max1=max(c[i]+cc[len(c)-i-1]-1,max1)
    print(len(a)-max1)

queue()
