class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        return sum(
            1 if operation[0] == "+" or operation[2] == "+" else -1
            for operation in operations
        )
