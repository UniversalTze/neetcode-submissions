class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # majority element is one that appears more than n/2. 

        # so essentially if we know that majority element will appear more than n/2 times
        # it will be the majority

        # so what we can do is keep an active count of things that exist in the array
        # if that count ever hits 0, we reset the majority element to the current
        # element. 

        # Becuase we know this property: majority element will appear more than n/2 times, 
        # we can assume that that element will always end with a positive count > 0, which 
        # would lead to it being returned. 

        curMaxEl = -1
        currentCount = 0
        for num in nums:
            if currentCount == 0:
                curMaxEl = num
                currentCount += 1
            else:
                if num == curMaxEl:
                    currentCount += 1
                else:
                    currentCount -= 1

        return curMaxEl
        

        