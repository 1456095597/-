def kkk():
    a=list(map(int,input().split()))
    n=a[0]
    r=a[1]
    avg=a[2]
    s=[]
    for i in range(n):
        s.append(list(map(int,input().split())))
    s1=0
    for i in s:
        s1+=i[0]
    if s1>=avg*n:
        print(0)
        return
    s.sort(key=lambda x:x[1])
    i=0
    s2=0
    while True:
        if s1+r-s[i][0]>=avg*n:
            s2+=(avg*n-s1-s[i][0])*s[i][1]
            print(s2)
            return
        else:
            s1+=r-s[i][0]
            s2+=(r-s[i][0])*s[i][1] 
        i+=1

while True:
    try:   
        kkk()
    except:
        break
            



