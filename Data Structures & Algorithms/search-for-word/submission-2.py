class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(count, position, xbound, ybound):
            nonlocal prevpositions
            pos = tuple(position)
            print(pos)
            print(count)
            if count == len(word):
                print("HERE")
                return True
            if position[0] < 0 or position[1] < 0 or position[0] >= ybound or position[1] >= xbound:
                return False # out of bounds search
            if board[position[0]][position[1]] != word[count]:
                return False
            if pos in prevpositions: # already been checked so no need
                return False
            if board[position[0]][position[1]] == word[count]:
                count += 1
                # set can't hold mutable items so convert list to an immutable object
                prevpositions.add(pos)
                if dfs(count, [position[0] + 1, position[1]], xbound, ybound) or \
                dfs(count, [position[0] - 1, position[1]], xbound, ybound) or \
                dfs(count, [position[0], position[1] - 1], xbound, ybound) or \
                dfs(count, [position[0], position[1] + 1], xbound, ybound):
                    return True
                prevpositions.remove(pos)
        found = False

        for y in range(len(board)):  # this loop is set to go through each combination
            for x in range(len(board[y])):
                if board[y][x] == word[0]:
                    prevpositions = set()
                    found = dfs(0, [y,x], len(board[y]), len(board))

                if found: # a combination has been found
                    return True
        return False
        