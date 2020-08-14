def kkk():
    a=list(input())
    x=0
    i=0
    while i<len(a):
        if a[i].isdigit():
            if x==0:
                a.insert(i,"*")
            x=1
        else:
            if x==1:
                a.insert(i,"*")
            x=0
        i+=1
    if a[len(a)-1].isdigit():a.append("*")
    print("".join(a))
    
while True:
    try:
        kkk()
    except:
        break
        