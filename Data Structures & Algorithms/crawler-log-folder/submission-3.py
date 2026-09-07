class Solution:
    def minOperations(self, logs: List[str]) -> int:
        counter = 0
        for index in range(len(logs)):
            if logs[index] == "../" and counter > 0:
                counter -= 1
            elif logs[index] != "../" and logs[index] != "./":
                counter += 1
        return counter