class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        wordpoint = 0
        abbrpoint = 0
        while abbrpoint != len(abbr):
            if abbr[abbrpoint] == word[wordpoint]: 
                wordpoint += 1
                abbrpoint += 1
            elif abbr[abbrpoint].isdigit():
                wordpoint += int(abbr[abbrpoint])
                abbrpoint += 1
                if wordpoint == len(word):
                    return True
                if wordpoint > len(word): 
                    return False

                if abbr[abbrpoint] != word[wordpoint]:
                    return False
            else: 
                return False
        return True
        
        
        