import sys

def maxProfit(prices):
    
    hashmap = dict()
    
    def recurse(day, owned):
        key = str(day) + ':' + str(owned)
        
        if key in hashmap:
            return hashmap[key]
        
        val = 0
        if day < len(prices):
            actions = []
            actions.append(recurse(day + 1, owned))
            if not owned:
              actions.append(recurse(day + 1, True) - prices[day])
            if owned:
                actions.append(prices[day])
            val = max(actions)                
            
        hashmap[key] = val
        return val
    
    x = recurse(0, False)
    print(hashmap)
    return x

def betterMaxProfit(prices):
  maxprofit = 0
  minprice = sys.maxsize

  for price in prices:
    if price < minprice:
      minprice = price
    elif price - minprice > maxprofit:
      maxprofit = price - minprice
  
  return maxprofit

print(maxProfit([7,1,5,3,6,4]))
print(betterMaxProfit([7,1,5,3,6,4]))