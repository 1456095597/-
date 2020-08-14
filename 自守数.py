def kkk():
    a=list(input())
    z=0
    for i in range(int("".join(a))+1):
        if i%10==1 or i%10==5 or i%10==6:
            s=i*i
            s1=list(str(i))
            s2=list(str(s))
            s2.reverse()
            s1.reverse()
            j=0
            for k in range(len(s1)):
                if s1[k]!=s2[k]:
                    j=1
                    break
            if j==0:
                z+=1
                print(i+1)
    print(z)

kkk()


        