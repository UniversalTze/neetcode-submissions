class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # idea use a map char -> (begin, next, end, k)
        # I only expected to grow to the right, however, it 
        # is a sliding window algo, so need to be able to move the left
        # one rather than rest. Hence why 'NEXT' was introduced. 
        BEGIN, NEXT, END, KVAL = 0, 1, 2, 3
        seen = {}
        result = 0

        for index in range(len(s)): 
            if s[index] in seen: # if character has been seen, need to update value in map
                char = s[index]
                value = seen[char]
                prevEnd = value[END]
                kVal = value[KVAL]
                nextVal = value[NEXT] # slide left hand side of window (was last case to consider)
                if (value[BEGIN] == value[NEXT]):
                    nextVal = index

                if index - prevEnd > 1: 
                    # more than 1 means, need to use a K value to reorganise
                    kVal -= index - prevEnd - 1
                    if kVal < 0:
                        # final case to move left window up
                        if k == (nextVal - value[BEGIN] - 1): 
                            data = (nextVal, nextVal, index, 0)
                            # set k to 0 any others should ruin this
                        else: 
                            data = (index, index, index, k) 
                        seen[s[index]] = data
                        continue
                # Only update end point as consecutive character seen       
                data = (value[BEGIN], nextVal, index, kVal) 
                if s[index] == 'S': 
                    print(data)
                seen[s[index]] = data
                result = max((index - value[BEGIN] + kVal) + 1, result)
                if result > len(s):  
                    # resulting string cannot be longer than original string as its replacing characters in a string
                    result = len(s)
            else: 
                data = (index, index, index, k)  # place value in map
                seen[s[index]] = data
                result = max(1 + k, result) # set highest count
        return result






        