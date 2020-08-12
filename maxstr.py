def maxstr():
    a=list(input())
    b=list(input())
    maxs=0
    m=[[0 for i in range(len(b)+1)] for i in range(len(a)+1)]
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i]==b[j]:
                m[i+1][j+1]=m[i][j]+1
                maxs=max(maxs,m[i+1][j+1])
    print(maxs)

maxstr()
