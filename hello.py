# -*- coding:utf-8 -*-
def Add(self, num1, num2): #第一题 不用符号的加法
    while num2!=0 :
        s1=num1^num2
        s2=(num1&num2)<<1  # 一边做异或一边做进位想与，进位想与的结果作为加数再次加，直到进位想与为0
        num1=s1
        num2=s2
    return num1
        # write code here

def cut(num):  #第二题 剪绳子 从最小的段便利最优化的解，直到整个绳子
    l=[]
    l.append(0)
    i=1
    while i<=num :
        l.append(i)
        j=1
        while j<i :
            l[i]=max(l[i],l[j]*l[i-j])
            j+=1
        i+=1
    return l[num]   

def multiplly(l=[]): #第三题 做数组乘法 以倒三角形式先乘下三角，再算上三角，注意数组下标的理解
    l2=[1]
    i=1
    while i<len(l) :
        l2.append(l[i-1]*l2[i-1])
        i+=1
    i-=1
    l3=1
    while i>0 :
        l3*=l[i]
        l2[i-1]*=l3
        i-=1
    return l2


def minMultiple(a,b):
    a1=a
    b1=b
    while a1!=b1:
        if a1>b1:
            a1=a1-b1
        else:
            b1=b1-a1
    a2=a/a1
    b2=b/b1
    return a2*b2*a1
            

def getCubeRoot(x):
    a=round(x/2,7)
    d=x
    b=round(0,7)
    c=round(0,7)
    while abs(a-c)>0.001 :
        c=a
        if a*a*a>x:
            d=a
            a=(a+b)/2
        else:
            b=a
            a=(a+d)/2
    return round(a,1)

def stringflip(s):
    l1=list(s)
    l1=list(reversed(l1))
    return "".join(l1)

def intflip():
    a=input()
    l1=list(a)
    l1=list(reversed(l1))
    print("".join(l1))


def reint():
    a=int(input())
    if 6-a>=19:
        print(int(a)+1)
    else:
        print(int(a))

def bincount():
    a=int(input())
    count=0
    while a/2!=0:
        if a%2==1:
            count=count+1
        a=int(a/2)    
    print(count)

def countlastword():
    a=list(input())
    count=a.count(" ")
    i=0
    countn=0
    while i<len(a):
        if count==0:
            print(len(a))
            break
        elif countn==count and count!=0:
            print(len(a)-i)
            break
        elif a[i]==" " :
            countn+=1
        i+=1
    
def countchar():
    a=list(input())
    b=input()
    if b.isdigit():
        count=a.count(b)
    else:
         count=a.count(b.upper())+a.count(b.lower())
    print(count)

def orderrandom():
    while True:
        try:
            a=int(input())
            i=0
            l=[]
            while i<a:
                l.append(int(input()))
                i+=1
            l.sort()
            i=0
            b=-222
            while i<a:
                if b==l[i]:
                    l.pop(i)
                    a-=1
                else:
                    b=l[i]
                    i+=1
            i=0
            while i<a:
                print(l[i])
                i+=1
        except:
            break

def cutstring():
    str1=input()
    str2=input()
    l1=list(str1)
    l2=list(str2)
    a=len(l1)
    ls=[]
    while True:
        if a<=8:
            i=0
            while i<8-a:
                l1.append("0")
                i+=1
            print("".join(l1))
            break
        else:
            i=0
            while i<8:
                ls.append(l1[0])
                l1.pop(0)
                i+=1
            print("".join(ls))
            ls.clear()
        a=len(l1)
    a=len(l2)
    while True:
        if a<=8:
            i=0
            while i<8-a:
                l2.append("0")
                i+=1
            print("".join(l2))
            break
        else:
            i=0
            while i<8:
                ls.append(l2[0])
                l2.pop(0)
                i+=1
            print("".join(ls))
            ls.clear()
        a=len(l2)

def hexchange():
    while True:
        try:
            a=int(input(),16)
            print(a)
        except:
            break

def findnum():
    a=int(input())
    l=[]
    if a==1:
        l.append(a)
    else:
        n=2
        while (a/n)!=1:
            if a%n==0 :
                l.append(n)
                a=a/n 
            else:
                n+=1
        l.append(n)
    i=0
    l1=[]
    while i<len(l):
        l1.append(str(l[i]))
        i+=1
    print(" ".join(l1))                  #.join切割只能为字符

def changecup():
    while True:
        try:
            a=int(input())
            b=0
            if a==0:
                break
            else:
                while int((a/3))!=0:
                    b+=int(a/3)
                    a=int(a/3)+int(a%3)
                    if a==2:
                        b+=1
                print(b)
        except:
            break

def nrabiat(x):
    if x==1:
        return 1
    elif x==2:
        return 1
    else:
        return nrabiat(x-1)+nrabiat(x-2)

def nrabiatsol():
    print(nrabiat(int(input())))


def count(s):
    
    i=len(s)-1
    s1=[]
    while i>=0:
        
        
        
        if s[i].isdigit() or s[i]=="+" or s[i]=="-" or s[i]=="*" or s[i]=="/" :
            s1.append(s[i])
            s.pop()
            i=len(s)-1

        elif s[i]=="{" or s[i]=="(" or s[i]=="[" :
            j=len(s1)-1
            while j>=0:
                if s1[j]=="+": 
                    s1.pop(j)
                elif s1[j]=="-":                  
                    sum=-int(s1[j-1] )
                    s1.pop(j)
                    s1[j-1]=sum   
                elif s1[j]=="*":                  
                    sum=int(s1[j-1] )*int(s1[j+1])
                    s1.pop(j)
                    s1.pop(j)
                    s1[j-1]=sum 
                elif s1[j]=="/":                  
                    sum=int(s1[j+1] )/int(s1[j-1])
                    s1.pop(j)
                    s1.pop(j)
                    s1[j-1]=sum 
                                 
                j-=1 
            sum=0
            j=0
            while j<len(s1):
                sum+=int(s1[j])
                j+=1
            return (sum,s)
        elif s[i]=="}" or s[i]=="]" or s[i]==")" :
            sn=s1
            s3=[]
            k=0
            while k<i:
                s3.append(str(s[k]))
                k+=1
            sum=count(s3)[0]
            s=count(s3)[1]
            sn.append(sum)
            s1=sn
            jj=len(s)-1
            while s[jj]!="{" and  s[jj]!="[" and s[jj]!="(" :
                s.pop()
                jj-=1
            s.pop()
            i=len(s)-1
        
    j=len(s1)-1
    while j>=0:
        if s1[j]=="+": 
            s1.pop(j)
        elif s1[j]=="-":                  
            sum=-int(s1[j-1] )
            s1.pop(j)
            s1[j-1]=sum  
        elif s1[j]=="*":                  
                sum=int(s1[j-1] )*int(s1[j+1])
                s1.pop(j)
                s1.pop(j)
                s1[j-1]=sum 
        elif s1[j]=="/":                  
            sum=int(s1[j+1] )/int(s1[j-1])
            s1.pop(j)
            s1.pop(j)
            s1[j-1]=sum     
        j-=1 
    sum=0
    j=0
    while j<len(s1):
        sum+=int(s1[j])
        j+=1
    return (sum,s)


def lll(s):
    i=0
    j=len(s)-1
    while i<j:
        if s[i].isdigit() and s[i+1].isdigit():
            s[i]=int(s[i])*10+int(s[i+1])
            s[i]=str(s[i])
            s.pop(i+1)
            j-=1
        else:
            i+=1
    return s   

def angelcreat(x):
    l=[[1],[1,1,1]]
    if x==1 or x==2:
        return 0
    else:
        i=2
        j=0
        jj=5
        while i<x:
            new=[]
            while j<jj:
                if j-2<0 or j-2>(len(l[i-1])-1):
                    a=0
                else:
                    a=l[i-1][j-2]
                if j-1<0 or j-1>(len(l[i-1])-1):
                    b=0
                else:
                    b=l[i-1][j-1]
                if j<0 or j>(len(l[i-1])-1):
                    c=0
                else:
                    c=l[i-1][j]
                new.append(a+b+c)
                j+=1
            l.append(new)
            i+=1
            jj+=2
            j=0
        l1=l[x-1]
        kk=0
        while kk<len(l1):
            if l1[kk]%2==0:
                return kk+1
            else :
                kk+=1
        return 0

def findperfectnum(n):
    i=2
    x=0
    while i<=n:
        j=2
        sum=0
        xx=int(i/2)
        while j<xx:
            if i%j==0:
                sum+=j
                sum+=int(i/j)
                xx=int(i/j)
            if sum>i:
                break
            j+=1
        if sum==i-1:
            x+=1
        i+=1
    print(x)           




def apples(m,n):
    sum=0
    if m<=0 or n<=0:
        return 0
    elif n==1 or m==1:
        return 1
    else:
        if m-n==0:
            sum=apples(m,n-1)+1
        else:
            sum=apples(m-n,n)+apples(m,n-1)
        return sum

i=4
m=[[0 for i in range(4)] for i in range(5)]


def kkkk():
    a=list(map(int,input().split()))
    x=a[1]
    a=list(map(int,input().split()))
    a.sort()
    print(" ".join(list(map(str,a[0:x]))))





