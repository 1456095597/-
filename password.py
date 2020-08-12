while True:
    try:
        a=list(input())
        sum=0
        x=0
        if len(a)<=4:
            sum+=5
        if 5<=len(a)<=7:
            sum+=10
        if len(a)>=8:
            sum+=25
        i=0
        tmp=0
        while i<len(a):
            if a[i].isdigit():
                tmp+=1
                x+=1
            i+=1
        if tmp==1:
            sum+=10
        elif tmp>=2:
            sum+=20
        i=0
        t1=0
        t2=0
        while i<len(a):
            if a[i].isalpha():
                if a[i].isupper():
                    t1=1
                else:
                    t2=1
                x+=1
            i+=1
        if (t1==1 and t2==0) or (t1==0 and t2==1):
            sum+=10
        elif t1==1 and t2==1:
            sum+=20
        if len(a)-x==1:
            sum+=10
        elif len(a)-x>1:
            sum+=25
        if (tmp!=0 and t1!=0 )or (tmp!=0 and t2!=0 ):
            if len(a)!=x:
                if t1==1 and t2==1:
                    sum+=5
                else:
                    sum+=3
            else:
                sum+=2
        if sum>=90:
            print("VERY_SECURE")
        elif 80<=sum<90:
            print("SECURE")
        elif 70<=sum<80:
            print("VERY_STRONG")
        elif 60<=sum<70:
            print("STRONG")
        elif 50<=sum<60:
            print("AVERAGE")
        elif 25<=sum<50:
            print("WEAK")
        else:
            print("VERY_WEAK")
    except:
        break

