def kkk():
    s=[]
    while True:
        try:
            a=input().split()
            for i in a:
                if s.count(i)==0:
                    s.append(i)
        except:
            break
    print(len(s))


kkk()
   

