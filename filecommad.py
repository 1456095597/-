def filecommad(t):
    if len(t)==1:
        if t[0] in "reset":
            print("reset what")
        else :
            print("unknown command")
    elif len(t)==2:
        if t[0] in "reset" and t[1] in "board":
            print("board fault")
        elif t[0] in "board" and t[1] in "add":
            print("where to add")
        elif t[0] in "board" and t[1] in "delete":
            print("no board at all")
        elif t[0] in "reboot" and t[1] in "backplane":
            print("impossible")
        elif t[0] in "backplane" and t[1] in "abort":
            print("install first")
        else:
            print("unknown command")




while True:
    try:
        t=input().split()
        filecommad(t)
    except :
        break
