class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # idea use a map char -> (begin, end, k)
        BEGIN, NEXT, END, KVAL = 0, 1, 2, 3
        seen = {}
        result = 0 # K is lowest it can for a character

        for index in range(len(s)): 
            if s[index] in seen:
                char = s[index]
                value = seen[char]
                prevEnd = value[END]
                kVal = value[KVAL]
                nextVal = value[NEXT]
                if (value[BEGIN] == value[NEXT]):
                    nextVal = index

                if index - prevEnd > 1: 
                    # more than 1 means, need to use a K value to reorganise
                    kVal -= index - prevEnd - 1
                    if kVal < 0: 
                        # final case to move left window up
                        if abs(kVal) == (nextVal - value[BEGIN] - 1): 
                            data = (nextVal, nextVal, index, 0) 
                            # set k to 0 any others should ruin this
                        else: 
                            data = (index, index, index, k) 
                        seen[s[index]] = data
                        continue
                # No need just update data like normal        
                data = (value[BEGIN], nextVal, index, kVal) 
                seen[s[index]] = data
                result = max((index - value[BEGIN] + kVal) + 1, result)
                if result > len(s): 
                    result = len(s)
            else: 
                data = (index, index, index, k) 
                seen[s[index]] = data
                result = max(1 + k, result)
        return result






        