class Solution:
    def validPalindrome(self, s: str) -> bool:

        def is_valid_palindrome(check: str):
            leftC = 0
            rightC = len(check) - 1
            print(check)
            while leftC < rightC: 
                if check[leftC] != check[rightC]:
                    return False
                leftC += 1
                rightC -= 1
            return True

        left = 0
        right = len(s) - 1
        res = True
        while left < right:
            if s[left] != s[right]:
                print(left)
                print(right)
                res = is_valid_palindrome(s[left:right]) or is_valid_palindrome(s[left+1:right+1])
                break
            left += 1
            right -= 1
        return res




        
        