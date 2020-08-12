
def move( n, x, y, z):  #将n个盘子从x借助y移动到z                                                       
    if 1 == n  :                                                        
        print(x,"-->",z)                                        
    else :                                                                 
        move(n-1,x,z,y)  #将n-1个盘子从x借助z移动到y
        print(x,"-->",z)           #将第n个盘子从x移动到z
        move(n-1,y,x,z)   #将n-1个盘子从y借助x移动到z
         

num=int(input("输入移动的圆盘数量"))
print("移动步骤如下:")
move(num,'X','Y','Z')
