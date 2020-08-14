def kkk(a,b):
    if (len(a)==1 and a[0]=="*" ) or (len(a)==1 and len(b)==1 and (a[0]==b[0] or a[0]=="?")):
        return True
    elif len(a)==1 or len(b)==1:
        if len(a)==1 :return False
        elif a[1]==b[0] and len(a)==2:return True
        else:return False
    elif a[0]==b[0] or a[0]=="?":
        return kkk(a[1:],b[1:])
    elif a[0]=="*":
        return kkk(a,b[1:]) or kkk(a[1:],b)

a=list(input())
b=list(input())
if kkk(a,b):print("true")
else :print("false")

