def kkk():
    c=""
    a=input().split(".")
    a=list(map(int,a))
    for i in range(len(a)):
        c+=(str(bin(a[i])).replace("0b","").rjust(8,"0"))
    print(int(c,2))
    a=int(input())
    c=(str(bin(a)).replace("0b","").rjust(32,"0"))
    s=[0]*4
    for i in range(len(s)):
        s[i]=int(c[8*i:8*i+8],2)
    print(".".join(list(map(str,s))))

while True:
    try:

        kkk()
    except:
        break