def maxProfit(prices: list[int]) -> int:
    minprice = prices[0]
    maxprofit = 0

    for i in prices:
        if i < minprice:
            minprice = i

        if i - minprice > maxprofit:
            maxprofit = i - minprice

    return maxprofit
    

print(maxProfit([7,6,4,3,1]))