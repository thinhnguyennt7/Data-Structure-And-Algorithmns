'''
Given a list of day stock prices (integers for simplicity), find the maximum single sell profit.

We need to maximize the single buy/sell profit and in case we can't make any profit, we'll try to minimize the loss.

Hint: Kadane's Algorithm

Input: [7,1,5,3,6,4]
Output: (1, 6)
Profit: 6 - 1 = 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.

'''
import sys
def find_buy_sell_stock_prices(stockPrices):

    # Initilize value
    minPrices = sys.maxsize # We have to set min to the maximun bound of integer
    maxProfit = 0

    for i in range(len(stockPrices)):

        # If that value in the array less then the minPrice then set that value become the minPrice
        if stockPrices[i] < minPrices:
            minPrices = stockPrices[i]

        # If that current value - the minPrice still greater that the maxProfit then set that value to the maxPrices
        elif stockPrices[i] - minPrices > maxProfit:
            maxProfit = stockPrices[i] - minPrices # Here is the profit
            maxPrices = stockPrices[i]

    #  If there are no transactions then output is where the lowest value and maxprices is 0
    if maxProfit == 0:
        return minPrices, 0

    # Return the min Price and the max Price
    return minPrices, maxPrices

print("Min and Max stock prices:", find_buy_sell_stock_prices([7,1,5,3,6,4]))
# OutPut: Min and Max stock prices: (1, 6)
# Similar problem: 121. Best Time to Buy and Sell Stock (Leetcode)

# Time: O(n)
# Memory: O(1)