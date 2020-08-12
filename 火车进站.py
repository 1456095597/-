b=[]
s=[]
ss=[]
sss=[]
def kkk(a):
    global b
    global s
    global ss
    global sss
    if len(a)==1:
        b.append(a[0])
        b.reverse()
        ss.extend(s)
        ss.extend(b)
        if sss.count("".join(ss))==0:sss.append("".join(ss))
        ss.clear()
        b.reverse()
        b.pop()
        return
    for i in range(3):
        if i==0:
            b.append(a[0])
            kkk(a[1:len(a)])
            b.pop()
        elif i==1:
            s.append(a[0])
            kkk(a[1:len(a)])
            s.pop()
        else :
            t1=[]
            t1=s.copy()
            s.append(a[0])
            t=[]
            t=b.copy()
            while len(b)!=0:
                b.reverse()
                s.append(b[0])
                b.pop(0)
                b.reverse()
                kkk(a[1:len(a)])
            b=t.copy()
            s=t1.copy()

            
  

a=input()
a=input().split()
kkk(a)
sss.sort()
for i in range(len(sss)):
    print(" ".join(sss[i]))
