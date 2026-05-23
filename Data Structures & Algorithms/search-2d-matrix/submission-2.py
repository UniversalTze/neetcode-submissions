class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        LOWER= 0 # lower bound of array inside matrix
        UPPER = len(matrix[0]) - 1
        
        start = 0
        end = len(matrix) - 1
        while start <= end:
            check = (start + end) // 2
            section = matrix[check]
            if section[LOWER] <= target and target <= section[UPPER]:
                # do something here
                left = LOWER
                right = UPPER 
                while left <= right:
                    #print("Here")
                    #break
                    #count = 0
                    mid = (left + right) // 2
                    #count += 1
                    if section[mid] == target:
                        return True
                    elif section[mid] < target:
                        left = mid + 1
                    else:
                        right = mid - 1
                break # no need to keep searching
                # as array to the right, lowerbound is alreay bigger than target
                # array to the left, upperbound is too small
            elif section[UPPER] < target:
                start = check + 1
            elif section[LOWER] > target:
                end = check - 1
    
        return False


        