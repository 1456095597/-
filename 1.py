# def kkk():
#     a=[11,5,6,8,9]
#     tmp=0
#     for i in range(len(a)):
#         for j in range(len(a)-i-1):
#             if a[j]>a[j+1]:
#                 a[j],a[j+1]=a[j+1],a[j]
#     print(a)

def kkk(): 
    arr=[11,5,6,8,9]
    for i in range(1,len(arr)):
        tag=arr[i]
        j=i-1
        while j>=0 and arr[j+1]<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=tag
    print(arr)

kkk()

