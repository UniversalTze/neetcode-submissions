class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i, j = 0, 0

        wordlen = len(word)
        abbrlen = len(abbr)
        while i < wordlen and j < abbrlen:
            if word[i] == abbr[j]:
                i += 1
                j += 1
            elif abbr[j].isalpha():
                return False
            else:
                firstind = j
                while j < abbrlen and abbr[j].isdigit():
                    j += 1
                i += int(abbr[firstind:j])
        return i == wordlen and j == abbrlen



