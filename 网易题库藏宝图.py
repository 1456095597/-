def kkk():
    a=list(input())
    b=list(input())
    for i in b:
        if i in a:
            x=a.index(i)
            a.remove(i)
            a=a[x:]
        else:
            print("No")
            return
    print("Yes")
    return

while True:
    try:
        kkk()
    except:
        break