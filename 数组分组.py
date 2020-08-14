s1=[]
s2=[]
s3=[]

def kkk():
    a=input()
    global s1
    global s2
    global s3
    a=list(map(int,input().split()))
    for i in range(len(a)):
        if a[i]%5==0 :s1.append(a[i])
        elif a[i]%3==0 :s2.append(a[i])
        else:s3.append(a[i])
    sum1=sum(s1)
    sum2=sum(s2)
    s3.sort()
    if lll(sum1,sum2,s3):print("true")
    else:print("false")

def lll(x,y,t):
    if len(t)==0 and x==y:return True
    elif len(t)==0 and x!=y:return False
    else:
        z=t[0]
        return lll(x+z,y,t[1:len(t)]) or lll(x,y+z,t[1:len(t)])

while True:
    try:
        kkk()
    except:
        break
  

    