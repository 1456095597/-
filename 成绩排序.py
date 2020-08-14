def kkk():
    a=int(input())
    b=input()
    s=[]
    for i in range(a):
        s.append(input().split())
    if b=="0":s.sort(key=lambda x:int(x[1]),reverse=True)
    else:s.sort(key=lambda x:int(x[1]))
    for i in range(len(s)):
        print(" ".join(s[i]))

def kkk1():
    a=list(input())
    for i in range(len(a)):
        if not(a[i].isalpha() or a[i]==" "):
            a[i]=" "
    a=list(str("".join(a)).split())
    a.reverse()
    print(" ".join(a))
kkk1()
   