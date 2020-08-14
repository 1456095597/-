def kkk():
    a=list(input())
    b=[["*" for i in range (2)]for j in range(len(a))]
    a.sort()
    j=0
    for i in range(len(a)):
        if a[i].isdigit() or a[i].isalpha() or a[i]==" ":
            if b[j][0]!=a[i] and b[i]=="*":
                b[j][0]=a[i]
                b[j][1]="1"
            elif  b[j][0]==a[i]:b[j][1]=str(int(b[j][1])+1)
            else:
                j+=1
                b[j][0]=a[i]
                b[j][1]="0"
    i=0
    while i < len(b):
        if b[i][0]=="*":
            b.pop(i)
        else:
            i+=1
    b.sort(key=lambda x:int(x[1]) ,reverse=True)
    
    c=[]
    s=[]
    for i in range(len(b)):
        if i==(len(b)-1):
            if b[i][1]!=b[i-1][1]:
                s.append(b[i][0])
            else:
                c.append(b[i][0])
                c.sort(key=ord)
                s.extend(c)

        elif b[i][1]!=b[i+1][1]:
            if len(c)!=0:
                c.append(b[i][0])
                c.sort(key=ord)
                s.extend(c)
               
                c.clear()
            else:s.append(b[i][0])
        else:
            c.append(b[i][0])
    
    print("".join(s))
kkk()
  


            
