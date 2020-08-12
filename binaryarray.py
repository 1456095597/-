def buyc():
    i=0 
    t=[]
    sum=0
    while i*5<=100:
        sum=i*5
        j=0
        while j*3<100:
            sum=sum+j*3
            k=0
            while True:
                if sum==100 and i+j+k*3==100:
                    t.append([i,j,k*3])
                    sum=5*i
                    break
                elif sum>100 or i+j+k*3>100:
                    sum=5*i
                    break
                k+=1
                sum=sum+1
            j+=1
        i+=1
    i=0
    while i<len(t):     
        print(" ".join(str(j) for j in t[i]))
        i+=1


def countday():
    aa=input().split()
    a=int(aa[0])
    b=int(aa[1])
    c=int(aa[2])
    sum=0
    if b==1:
        sum=c
    elif b==2:
        sum=31+c
    elif b==3:
        if a%4==0:
            sum=60+c
        else :
            sum=59+c
    elif b==4:
        if a%4==0:
            sum=91+c
        else :
            sum=90+c
    elif b==5:
        if a%4==0:
            sum=121+c
        else :
            sum=120+c
    elif b==6:
        if a%4==0:
            sum=152+c
        else :
            sum=151+c
    elif b==7:
        if a%4==0:
            sum=182+c
        else :
            sum=181+c
    elif b==8:
        if a%4==0:
            sum=213+c
        else :
            sum=212+c
    elif b==9:
        if a%4==0:
            sum=244+c
        else :
            sum=243+c
    elif b==10:
        if a%4==0:
            sum=274+c
        else :
            sum=273+c
    elif b==11:
        if a%4==0:
            sum=305+c
        else :
            sum=304+c
    elif b==12:
        if a%4==0:
            sum=335+c
        else :
            sum=334+c
    return sum
    

    
while True:
    try:
        x=0
        max=0
        a=int(input())
        while a!=0:
            if a%2!=0:
                x+=1
                if x>max:
                    max=x
            else:
                x=0
            a=int(a/2)
        print(max)
    except:
        break