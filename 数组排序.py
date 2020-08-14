def kkk():
    a=input()
    a=list(map(int,input().split()))
    b=input()
    a.sort()
    if b=="1":a.reverse()
    print(" ".join(list(map(str,a))))

while True:
    try:
        kkk()
    except:
        break