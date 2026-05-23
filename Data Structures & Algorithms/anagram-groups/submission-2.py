class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # strs only lower case letters (so can intialise an array and have each index represent a number)
        # just represents how may times a character appears in the array and is just a way
        # of building an encode string for anagram. 
        NUMBER_OF_LETTERS = 26
        encodedMap = {}
        for string in strs:
            encode = [0] * 26
            for char in string: 
                # use a reference point to ensure that chracters that count sums to are appropriately handled to their corresponding index
                pos = (ord('A') - ord(char)) % NUMBER_OF_LETTERS
                encode[pos] += 1
            encode = [str(x) for x in encode]
            # Used a dot to seperate spaces where number for of characters make the same strings.
            # e.g 11 a's and 1 b or 1 a and 11 b's
            encoded_str = ".".join(encode)
            print(encoded_str)

            # check map if encoded string exists in map
            if encoded_str in encodedMap: # if exists append string to list of strings
                encodedMap.get(encoded_str).append(string)   # to dictionary list
            else: 
                encodedMap[encoded_str] = [string]
        return list(encodedMap.values())        