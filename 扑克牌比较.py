def kkk():
    a=input().split("-")
    a[0]=a[0].replace("10","Z")
    a[1]=a[1].replace("10","Z")
   

    D = {'3':0, '4':1, '5':2, '6':3, '7':4, '8':5, '9':6, 'Z':7, 'J':8, 'Q':9, 'K':10, 'A':11, '2':12, 'joker':13, 'JOKER':14}
    if a[0][0].islower():
        print(a[0])
    elif a[1][0].islower():
        print(a[1])
    elif len(a[0])==len(a[1]):
        if D[a[0][0]]>D[a[1][0]]:
            a[0]=a[0].replace("Z","10")
            print(a[0])
        else:
            a[1]=a[1].replace("Z","10")
            print(a[1])
    elif len(a[0])==7:
        a[0]=a[0].replace("Z","10")
        print(a[0])
    elif len(a[1])==7:
        a[1]=a[1].replace("Z","10")
        print(a[1])
    else:print("ERROR")


kkk()
 