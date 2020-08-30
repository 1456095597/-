def kkk():
    a=list(input().split(","))
    if a[0]=="{}":
        return 0
    b=len(a)
    i =1
    j=1
   
    while b>0:
        b=b-i
        i=i*2
        j+=1
    return j-1

while True:
    try:
        print(kkk())
    except:
        break