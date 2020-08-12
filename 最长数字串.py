def kkk():
    a=list(input())
    x=[]
    max1=0
    c=[]
    s=""
    for i in range(len(a)):
        if i==0 and a[i].isdigit():
            x.append(1)
        elif i==0 and not(a[i].isdigit()):
            x.append(0)
        else:
            if a[i].isdigit():x.append(x[i-1]+1)
            else:x.append(0)
        if x[i]>max1:
            max1=x[i]
            c.clear()
            c.append(i)
        elif x[i]==max1:
            c.append(i)
    for i in range(len(c)):
        s+="".join(a[c[i]-max1+1:c[i]+1])
   
    print(s+","+str(max1))
while True:
    try:
        kkk()
    except:
        break
       