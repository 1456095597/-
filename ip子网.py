def kkk():
    a=input().split(".")
    for i in range(len(a)):
        a[i]=bin(int(a[i])).replace("0b","").rjust(8,"0")
    a1="".join(a)
    a=input().split(".")
    for i in range(len(a)):
        a[i]=bin(int(a[i])).replace("0b","").rjust(8,"0")
    a2="".join(a)
    a=input().split(".")
    for i in range(len(a)):
        a[i]=bin(int(a[i])).replace("0b","").rjust(8,"0")
    a3="".join(a)
    s1=""
    s2=""
    a1=list(a1)
    a2=list(a2)
    a3=list(a3)
    for i in range(len(a1)):
        if a1[i]=="1" and a2[i]=="1":
            s1+="1"
        else:s1+="0"
    for i in range(len(a1)):
        if a1[i]=="1" and a3[i]=="1":
            s2+="1"
        else:s2+="0"
    if s1==s2:print("0")
    else:print("2")
while True:
    try:
        kkk()
    except:
        break