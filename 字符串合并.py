def jjj():
    a=input().split()
    str1=a[0]+a[1]
    l1=list(str1)
    b=[]
    c=[]
    for i in range(len(l1)):
        if i%2==0:
            c.append(l1[i])
        else:
            b.append(l1[i])
    c.sort()
    b.sort()
    for i in range(len(l1)):
        if i%2==0:
            l1[i]=c[0]
            c.pop(0)
        else :
            l1[i]=b[0]
            b.pop(0)  
    for i in range(len(l1)):
        if l1[i] in "0123456789abcdefABCDEF":
            l2=[]
            x=int(l1[i],16)
            while int(x/2)!=0:
                l2.append(str(int(x%2)))
                x=x/2
            l2.append(str(int(x%2)))
            while len(l2)<4:
                l2.append(str(0))
            s=str(hex(int("".join(l2),2))).replace("0x","").upper()
            l1[i]=s
           

    print("".join(l1))

while True:
    try:

        jjj()
    except:
        break
