ss=[]
def find24(a,s):
    global ss
    if len(a)==1:
        if a[0]==s:
            ss.append(a[0])
            return True
        else:return False
    else:
        for i in range(len(a)):
            x=a[i]
            aa=a[:i]+a[i+1:]
            if find24(aa,s+x):
                ss.append("-")
                ss.append(x)
            
                return True
            elif find24(aa,s-x):
                ss.append("+")
                ss.append(x)
              
                return True
            elif find24(aa,s*x):
                ss.append("/")
                ss.append(x)
               
                return True
            elif find24(aa,s/x):
                ss.append("*")
                ss.append(x)
                
                return True
                
        return False


while True:
    try:
        a=input().replace("A","1").replace("J","11").replace("Q","12").replace("K","13").split()
        x=0
        for i in range(len(a)):
            if not a[i].isdigit():
                print("ERROR")
                x=1
        a=list(map(int,a))
        if x==0:  
            if find24(a,24):print("".join(list(map(str,ss))).replace("1","A").replace("11","J").replace("12","Q").replace("13","K"))
            else :print("NONE")
    except:
        break
