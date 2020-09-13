def kkk():
    w= [0 , 2 , 3 , 4 , 5 ]			#商品的体积2、3、4、5
    v = [0 , 3 , 4 , 5 , 6 ]		#商品的价值3、4、5、6
    bagV = 8;					        #背包大小
    dp = [[0 for i in range(9) ]for i in range(5)]		       #动态规划表 ，注意新建二维数组方法
    max1=0
    for i in range (5):
        for j in range(bagV+1):
            if j < w[i]:
                    dp[i][j] = dp[i - 1][j]
            else:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w[i]] + v[i])
            max1=max(dp[i][j],max1)
    print(max1)
    print(dp)
    
kkk()