def findm():
    a=list(input())
    b=list(input())
    aa=[]
    x=0
    if len(a)>len(b):
        aa=b
        b=a
        a=aa
    max1=0
    c=[[0 for i in range(len(b)+1)] for j in range(len(a)+1)]
   
    for i in range(len(a)):
        for j in range(len(b)):
            if i==0 or j==0:
                if a[i]==b[j]:c[i][j]=1
            else:
                if a[i]==b[j]:c[i][j]=c[i-1][j-1]+1
            if c[i][j]>max1:
                max1=c[i][j]
                x=i
               
    s=[]
    i=0
    
    while i<max1:
        s+=a[x]
        x=x-1
        i+=1
    s.reverse()
    print("".join(s))



findm()
  
            



        
