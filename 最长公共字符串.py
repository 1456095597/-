def findn():
    a=list(input())
    b=list(input())
    d=[[0 for i in range(len(b))] for j in range(len(a))]
    max1=1
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i]==b[j] :
                if i==0 or j==0:
                    d[i][j]=1
                else:d[i][j]=max1+1
            max1=max(max1,d[i][j])
    if len(a)>len(b): x=len(a) 
    else:x=len(b)
    print(x-max1)

findn()
