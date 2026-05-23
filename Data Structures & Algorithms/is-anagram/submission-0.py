class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # O(1) space -> use of an array that doesn't grow
        ALPHABET_CHARACTERS = 26

        # Create an array with 26 0's 
        checker = [0] * ALPHABET_CHARACTERS 

        # 1st step add 1 to all indexes (ascii % 26 to get their index in the array)
        for i in s: 
            index = ord(i) % ALPHABET_CHARACTERS
            checker[index] += 1
        
        # 2nd step: 
        # Loop through next string and minus the character indexes from the counter array
        for a in t:
            index = ord(a) % ALPHABET_CHARACTERS
            checker[index] -= 1
        
        return checker.count(0) == ALPHABET_CHARACTERS

        

        