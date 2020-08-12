def she():
    a=int(input())
    b=[[0 for i in range(a)]for j in range(a)]
    for i in range(a):
        j=0
        while j<=a-i-1:
            if i==0 and j==0:b[i][j]=1
            elif i==0:b[i][j]=b[i][j-1]+j+1
            else:b[i][j]=b[i-1][j+1]-1
            j+=1
    for i in range(len(b)):
        j=i

        while j>0:
            b[i].pop()
            j-=1
        print(" ".join(list((map(str,b[i])))))

def find7():
    a=int(input())
    x=0
    for i in range(a+1):
        if i%7==0:
            x+=1
           
        elif  list(str(i)).count("7")>0:
            x+=1
           
    print(x-1)

while True:
    try:
 
        find7()
    except:
        break


