import re
def chec():
    a=list(input())
    t1=0
    t2=0
    t3=0
    t4=0
    if len(a)<=8:
        return "NG"
    for i in range(len(a)):
        if a[i].isdigit():
            t1+=1
        elif a[i].isalpha():
            if a[i].isupper():
                t2+=1
            else:
                t3+=1
    if len(a)-t1-t2-t3 !=0:
        t4=1
    if t1>0:
        t1=1
    if t2>0:
        t2=1
    if t3>0:
        t3=1
    if t1+t2+t3+t4<3:
        return "NG"
    a="".join(a)
    if re.match(".*(...)(....)(.*\\2)(.*\\1).*",a)!=None:
        return "NG"
    return "OK"

while True:
    try:
        if re.match(".*(...)(....)(.*\\2)(.*\\1).*",input())!= None:
            print("yyy")
        else:
            print("NNN")
    except:
        break

