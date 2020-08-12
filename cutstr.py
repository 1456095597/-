def countk():
    a=list(input().upper())
    a.reverse()
    i=0
    while i <len(a):
        if a.count(a[i])!=1:
            a.remove(a[i])
        else:
            i+=1
    a.reverse()
    for i in range(65,91):
        if chr(i) not in a:
            a.append(chr(i))
    print(a)
    b=input()
    for i in b:
        if i.isupper():
            res+=a[ord(i)-65]
        if i.islower():
            res+=a[ord(i)-97].lower()
    
    print(res)
  
  

countk()
