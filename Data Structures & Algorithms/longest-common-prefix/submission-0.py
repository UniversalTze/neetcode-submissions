class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = {}
        string = strs[0]
        strindex = 0
        while strindex < len(string):
            pre = string[0:strindex + 1]
            prefix[pre] = 1
            strindex += 1
        
        for index in range(1, len(strs)):
            string = strs[index]
            strindex = 0
            while strindex < len(string):
                pref = string[0:strindex + 1]
                if pref in prefix:
                    prefix[pref] += 1
                else: 
                    break
                strindex += 1
        res = ""
        for key, value in prefix.items():
            if value == len(strs):
                if len(key) >= len(res):
                    res = key
        print(prefix)
        return res