def fileorder():
    a=int(input())
    b=[]
    for i in range(a):
        b.append(list(input()))
    b.sort()
    for i in range(len(b)):
        print("".join(b[i]))

def flipstr():
    a=input().split()
    i=len(a)-1
    c=[]
    while i>=0:
        c.append(a[i])
        i-=1
    print(" ".join(c))


while True:
    try:
        flipstr()
    except:
        break
