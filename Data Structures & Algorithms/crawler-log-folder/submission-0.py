class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for index in range(len(logs)):
            if logs[index] == "../" and len(stack) > 0:
                stack.pop()
            elif logs[index] != "../" and logs[index] != "./":
                stack.append(logs[index])
        return len(stack) 