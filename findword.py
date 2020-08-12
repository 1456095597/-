def moved():
    x=0
    y=0
    a=input().split(";")
    for i in range(len(a)):
        b=list(a[i])
        if len(b)==3:
            if b[1].isdigit() and b[2].isdigit():
                b[1]=int(b[1])*10+int(b[2])
                b[1]=str(b[1])
                b.pop()
        if len(b)==2:
            if b[0]=="A" and b[1].isdigit():
                x-=int(b[1])
            elif b[0]=="D" and b[1].isdigit():
                x+=int(b[1])
            elif b[0]=="W" and b[1].isdigit():
                y+=int(b[1])
            elif b[0]=="S" and b[1].isdigit():
                y-=int(b[1])
    print("%d,%d"%(x,y))

while True:
    try:

        moved()
    except:
        break

