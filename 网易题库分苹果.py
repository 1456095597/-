def kkk():
    a=int(input())
    b=list(map(int,input().split()))
    sum=0
    for i in b:
        sum+=i
    if sum%a!=0:
        print(-1)
        return
    else:
        sum=sum//a
        x=0
        for i in b:
            if (i-sum)%2!=0:
                print(-1)
                return
            else:
                x+=abs((i-sum)//2)
        print(x//2)       
        return
while True:
    try:
        kkk()
    except:
        break
        

