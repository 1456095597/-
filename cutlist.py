def cut1():
    a=list(input())
    b=[]
    for i in range(len(a)):
        if len(b)==0:
                b.append(a[i])
        for j in range(len(b)):
            if ord(a[i])<ord(b[j]):
                b.insert(j,a[i])
                break
            if j==(len(b)-1) and i!=0:
                b.append(a[i]) 

    print("".join(b))


def finda():
    x=0
    a=list(input())
    for i in range(len(a)):
        if a.count(a[i])==1:
            print(a[i])
            x=1
            break
    if x==0 :print(-1)

def isda(n):
    x=0
    i=2
    while i*i<=n:
        if n%i==0:
            x=1
            break
        i+=1
    if x==1:return False
    else :return True

def findb():
    a=int(input())
    i=2
    x=0
    while i*2<a:
        if isda(i):
            if isda(a-i):
                x=i
        i+=1
    print(x)
    print(a-x)



findb()
   
  
