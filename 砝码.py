def kkk():
    a=int(input())
    x=list(map(int,input().split()))
    y=list(map(int,input().split()))
    n=sum(y)
    s=[]
    ans=[0]
    for i in range(len(y)):
        for j in range(y[i]-1):
            x.append(x[i])
  
    for i in x:
        temp = set(ans)
        for j in temp:
            ans.append(j+i)
        # 去重
    print(len(set(ans)))

while True:
    try:
        kkk()
    except:
        break