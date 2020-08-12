def kkk():
    a=input()
    a=list(map(int,input().split()))
    b=input()
    b=list(map(int,input().split()))
    a.extend(b)
    
    a=list(set(a))
    a.sort()
    print("".join(list(map(str,a))))

while True:
    try:
        kkk()
    except:
        break