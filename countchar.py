def countchar():
    a=list(input())
    b=[]
    for i in range(len(a)):
        if b.count(a[i])==0:
            b.append(a[i])
    print(len(b))

def listadd():
    a=int(input())
    l=dict()
    d=[]
    for i in range(a):
        t=input().split()
        b=int(t[0])
        if d.count(b)==0:
            d.append(b)
        c=int(t[1])
        if b in l:
            l[b]+=c
        else:
            l[b]=c
    d.sort()
    for i in range(len(d)):
        print("%d %d"%(d[i],l[d[i]]))

def password():
    a=list(input())
    for i in range(len(a)):
        if a[i].isupper():
            a[i]=a[i].lower()
            if a[i]=="z":
                a[i]="a"
                i+=1
            else:
                a[i]=chr(ord(a[i])+1)
        elif a[i]=="z" or a[i]=="x" or a[i]=="y" or a[i]=="w":
            a[i]="9"
        elif a[i]=="a" or a[i]=="b" or a[i]=="c" :
            a[i]="2"
        elif a[i]=="d" or a[i]=="e" or a[i]=="f" :
            a[i]="3"
        elif a[i]=="g" or a[i]=="h" or a[i]=="i" :
            a[i]="4"
        elif a[i]=="j" or a[i]=="k" or a[i]=="l" :
            a[i]="5"
        elif a[i]=="m" or a[i]=="n" or a[i]=="o" :
            a[i]="6"
        elif a[i]=="p" or a[i]=="q" or a[i]=="r" or a[i]=="s" :
            a[i]="7"
        elif a[i]=="v" or a[i]=="t" or a[i]=="u" :
            a[i]="8"
    print("".join(a))

def flipint():
    a=list(input())
    i=len(a)-1
    b=[]
    while i>=0:
        if b.count(a[i])==0:
            b.append(a[i])
        i-=1
    print(int("".join(b)))
    
while True:
    try:
        flipint()
    except:
        break