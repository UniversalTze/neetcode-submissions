class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # use a recusrive function to create the possibel outcomes
        OPEN = "("
        CLOSED = ")"
        res = set() # stop any duplicates from being added
        arr = []
    
        # in parentheses, the closed count cannot ever be more than the open count, if so we
        # have an issue/
        # if closed coutn and open count == 3, then we can append it to a result list
        def recurParenthesis(arr, opencount, closedcount):
            nonlocal res
            if opencount == n and closedcount == n:
                res.add(''.join(arr))
                return
            if opencount != n: 
                # append all open braces first so first one will be "((()))"
                # the recursion will back track from this and do what needs to be done. 
                opencount += 1
                arr.append(OPEN)
                recurParenthesis(arr, opencount, closedcount)
                arr.pop()
                opencount -= 1
            if closedcount < opencount:
                closedcount += 1
                arr.append(CLOSED)
                recurParenthesis(arr, opencount, closedcount)
                arr.pop()
                closedcount -= 1
        recurParenthesis(arr, 0, 0)
        return list(res)
            
                
        