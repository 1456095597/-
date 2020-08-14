def kkk():
    a=input()
    a=list(input().split())
    b=input()
    b=list(input().split())
    c=[0]*len(a)
    z=0
    for i in range(len(b)):
        if a.count(b[i])!=0:
            c[a.index(b[i])]+=1
        else:z+=1
    for i in range(len(a)):
        print("%s : %d"%(a[i],c[i]))
    print("Invalid : %d"%z)



kkk()
  