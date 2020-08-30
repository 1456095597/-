def find24(a,s):
    if len(a)==0:
        if s==24:return True
        else:return False
    else:
        for i in range(len(a)):
            x=a[i]
            aa=a[:i]+a[i+1:]
            if find24(aa,s+x) or find24(aa,s-x) or find24(aa,s*x) or find24(aa,s/x):
                return True
        return False

while True:
    try:
        a=list(map(int,input().split()))
        if find24(a,0):print("true")
        else :print("false")
    except:
        break