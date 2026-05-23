class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # using dp array and backtracking.

        # if we went forward, have to check every substring  O(n^2) is in 
        # wordDict when moving forward. Leading to O(n^2 * w * l) where 
        # w is the words in dictionary and l is the length of longest word in 
        # wordDict
        
        # when backtracking, we set dparray[len(s)] = True, which indicates if you can 
        # get to this then set current index in iteration to true

        dparray = [False] * (len(s) + 1)
        dparray[len(s)] = True

        for index in range(len(s) - 1, -1, -1):
            for word in wordDict:
                if index + len(word) > len(s):
                    # out of bounds, thus no need to process
                    continue
                if s[index: index + len(word)] == word and not dparray[index]:
                    # slicing is only inclusive of lower end and exclusive of upper end
                    # so if index = 0 and len(w) = 4, domain = [0, 3]

                    # if dparray has been set to true, no need to check again as it can reach the end 
                    # or access indexes that can reach the end. 
                    dparray[index] = dparray[index + len(word)]
                    # the idea of this backtracking is that if a string is found
                    # check that at the index next to the end of the string can reach the or is true
                    # is true means that it can reach the end and therefore be partitioned. 

                    # e.g "NeetCode", wordDict: [Neet, Code]
                    # dp = [F, F, F, F, F, F, F, F, T]
                    # dp = [F (N), F(E), F(E), F(T), F(C), F(O), F(D), F(E), T] -> iterate until Code is found
                    # when "Code" is found, it checks dp[index] = dp[index + len(Code)] which is True
                    # this means that at index where C (index 4) forms the substring "Code", can reach the end
                    # Any other index that can paritition the remaining string with words in WordDict
                    # can reach the end index of the original string, if they land on this index that has been 
                    # found to be true. (True power of DP -> No need to check again at Code because it's been done) 

        return dparray[0]
        