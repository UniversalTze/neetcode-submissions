class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        charsMap = {}
        lengthOfWords = 0
        for char in chars:
            charsMap[char] = charsMap.get(char, 0) + 1

        for index in range(len(words)):
            word = words[index]
            if len(word) > len(chars): 
                continue

            char_count = Counter(word)
            count = True

            for key, value in char_count.items():
                if key not in charsMap: 
                    count = False
                    break
                if key in charsMap and value > charsMap[key]:
                    count = False
                    break

            if count:
                lengthOfWords += len(word)

        return lengthOfWords
            
        
        
        