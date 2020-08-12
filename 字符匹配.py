def kkk():
    a=list(input())
    b=list(input())
    for i in range(len(a)):
        if b.count(a[i])==0:
            return "false"
    return "true"


print(kkk())
        
   