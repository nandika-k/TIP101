def max_profit(prices):
	
    
    max_price = 0
    i = 0
    for price in prices:
        curr_max = max(prices[i:])
        profit = curr_max - price
        if profit > max_price:
            max_price = profit
        i += 1
    return max_price
    
    

prices = [7,1,5,3,6,4]
print(max_profit(prices))