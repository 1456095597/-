def kkk():
    a=input()
    b=input()
    c=[[0 for i in range(len(a)+1)]for j in range(len(b)+1)]
    for i in range(len(a)+1):
        c[0][i]=i
    for j in range(len(b)+1):
        c[j][0]=j
    for i in range(1,len(b)+1):
        for j in range(1,len(a)+1):
            c[i][j]=min(c[i-1][j-1]+(a[j-1]!=b[i-1]),c[i-1][j]+1,c[i][j-1]+1)
    print(c[-1][-1])

while True:
    try:
        kkk()
    except:
        break
