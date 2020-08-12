def kkk():
    a=list(input())
    for i in range(len(a)):
        if a[i].isdigit():
            if a[i]=="9":
                a[i]="0"
            else: a[i]=chr(ord(a[i])+1)
        else:
            if ord(a[i])>96:
                if a[i]=="z":a[i]="A"
                else:
                    a[i]=chr(ord(a[i])-31)
            else:
                if a[i]=="Z":a[i]="a"
                else:
                    a[i]=chr(ord(a[i])+33)
    print("".join(a))
    a=list(input())
    for i in range(len(a)):
        if a[i].isdigit():
            if a[i]=="0":
                a[i]="9"
            else: a[i]=chr(ord(a[i])-1)
        else:
            if ord(a[i])>96:
                if a[i]=="a":a[i]="Z"
                else:
                    a[i]=chr(ord(a[i])-33)
            else:
                if a[i]=="A":a[i]="z"
                else:
                    a[i]=chr(ord(a[i])+31)
    print("".join(a))

while True:
    try:
        kkk()
    except:
        break