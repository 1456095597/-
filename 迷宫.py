m= []
s= []
smin=[0]*999
def smz(i,j):
    global smin,s
    if i==len(m)-1 and j==len(m[0])-1:
        if len(s)<len(smin):
            smin=s
    else:
        m[i][j]=1
        if j+1<len(m[0]) and m[i][j+1]==0:
            s.append([i,j+1])
            smz(i,j+1)
        elif i+1<len(m) and m[i+1][j]==0:
            s.append([i+1,j])
            smz(i+1,j)
        elif i-1>=0 and  m[i-1][j]==0:
            s.append([i-1,j])
            smz(i-1,j)
        elif i-1>=0 and  m[i][j-1]==0:
            s.append([i,j-1])
            smz(i,j-1)
        else:
            m[i][j]=0
            s.pop()

def maze():
    global m
    a=input().split()
    x=int(a[0])
    y=int(a[1])
    m= [[0 for i in range(y)] for j in range(x)]
    for i in range(x):
        t=input().split()
        for j in range(len(t)):
            if t[j]=="0":
                m[i][j]=0
            else:
                m[i][j]=1
    
    smz(0,0)

maze()
print("(0,0)")
for i in range(len(smin)):
    print("(%d,%d)"%(smin[i][0],smin[i][1]))
s.clear()
smin.clear()
m.clear()
