class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lower = 1 # lower is the lowest speed of eating bananas per hour
        # this occurs when hours >= sum(all bananas in ith pile)
        # minimum eating speed to consume bananas
        maximum = 0 # this is the maximum. this is maximised when piles.length = hours
        # as it needs to be able consume bananas within every pile.
        # having maximum number of all piles ensures this
        res = 0 # result
        for i in range(len(piles)): # O(N)
            if maximum < piles[i]:
                maximum = piles[i]
        
        if h == (len(piles)):
            return maximum
           
        # now that we have a range, we can do a binary search to find minimum 
        # value/rate to eat all bananas within the timeframe
        count = 0
        while lower <= maximum:# log m
            mid = (lower + maximum) // 2 # this is the rate
            hours = 0
            #print(mid)
            for i in range(len(piles)):
                remainder = piles[i] % mid
                if piles[i] > mid:
                    hours += piles[i] // mid
                    if remainder > 0:
                        hours += 1
                else:
                    hours += 1
            if hours <= h: # this bloody equals
                # this means that current rate, consumes it within the given timeframe
                # so we don't need to worry about maximum can move upper down to mid
                maximum = mid - 1
                if res == 0:
                    res = mid
                else:
                    res = min(res, mid)
            # current rate does not fit within timeframe, so need to increase rate, by moving lower to mid       
            else:
                lower = mid + 1
            
        return res
        