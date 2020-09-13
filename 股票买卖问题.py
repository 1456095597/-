class Solution {
    public int maxProfit(int[] prices) {
        int fstBuy = Integer.MIN_VALUE, fstSell = 0;
        int secBuy = Integer.MIN_VALUE, secSell = 0;
        for(int i = 0; i < prices.length; i++) {
            fstBuy = Math.max(fstBuy, -prices[i]);
            fstSell = Math.max(fstSell, fstBuy + prices[i]);
            secBuy = Math.max(secBuy, fstSell -  prices[i]);
            secSell = Math.max(secSell, secBuy +  prices[i]); 
        }
        return secSell;

    }
}

class Solution {
    public int maxProfit(int[] prices) {
        if(prices.length <= 1)
            return 0;
        int buy = -prices[0], sell = 0;
        for(int i = 1; i < prices.length; i++) {
            sell = Math.max(sell, prices[i] + buy);
            buy = Math.max( buy,sell - prices[i]);
        }
        return sell;
    }
}