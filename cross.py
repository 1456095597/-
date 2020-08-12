def cross(m,n):
    if m==0 or n==0:
        return 1
    else:
        return cross(m-1,n)+cross(m,n-1)

def kkk():
    a=int(input())
    i=0
    while i<a:
        if a%2==0:
            b=a*a+(i-int(a/2)+1)*2-1
            if  i==(a-1):
                print(b,end='')
            else:
                print("%d+"%(b),end='')
        else:
            b=a*a+(i-int(a/2))*2
            if  i==(a-1):
                print(b,end='')
            else:
                print("%d+"%(b),end='')
        i+=1
def filecut():
    t=input().split()
    i=0
    while i<len(t):
        if t[i][0]=="\"":
            t[i].pop(0)
            t[i].pop()
        i+=1
    i=0
    print(len(t))
    while i<len(t):
        print(t[i])
        i+=1
filecut()
