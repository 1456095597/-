def finda():
    a=list(input())
    b=int(input())
    max1=0
    t=0
    x=0
    for i in range(len(a)):
        t=0
        for j in range(b):
            if i+j<len(a):
                if a[i+j]=="C" or a[i+j]=="G":
                    t+=1
        if t>max1:
            x=i
            max1=t
    print("".join(a[x:x+b]))
while True:
    try:
        finda()
    except:
        break


