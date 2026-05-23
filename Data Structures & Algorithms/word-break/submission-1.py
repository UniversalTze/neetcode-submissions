class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dparray = [False] * (len(s) + 1)
        startIndex = 0
        wordSet = set(wordDict)
        # last index is true, if you can get to last index, can return true
        dparray[len(s)] = True
        for index in range(len(s), -1, -1):
            # bottom up approach from end of string
            for w in wordSet:
                if index + len(w) > len(s):
                    continue
                print(s[index: index + len(w)])
                if s[index: index + len(w)] == w and not dparray[index]:
                    # found a word, check the index that comes one after it 
                    # to see if a word has been sliced and matched to a word 
                    # in the index
                    dparray[index] = dparray[index + len(w)]
                    # for the case of the first word is being matched, that last index has been set
                    # to true as the if you can get to last index, can return true
        return dparray[0]
        