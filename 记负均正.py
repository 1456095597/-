def main():
    count=0
    avg=0.0
    count1=0
    sum=0
    while True:
        try:
            num=int(input())
            if num<0:
                count+=1
            else:
                sum=sum+num
                count1+=1
                avg=sum/count1
                average=round(avg,1)
        except:
            break
    return count,average
 
c,a=main()
print(c)
print(a)
