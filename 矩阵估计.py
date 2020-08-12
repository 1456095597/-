def kkk():
    a=int(input())
    x=[]
    for i in range(a):
        x.append(list(map(int,input().split())))
    b=list(input())
    c=[]
    sum=0
    j=0
    for i in range(len(b)):
        if b[i].isalpha():
            c.append(x[j])
            j+=1
        elif b[i]==")":
            while len(c)!=1:
                sum+=c[len(c)-1][0]*c[len(c)-2][0]*c[len(c)-1][1]
                c.append([c[len(c)-2][0],c[len(c)-1][1]])
                c.pop(len(c)-3)
                c.pop(len(c)-2)

    print(sum)
while True:
    try:

        kkk()
    except:
        break


