class Solution:
    def minOperations(self, boxes: str) -> list[int]:
        n = len(boxes)

        acc = 0
        ones = 0

        operations = [0] * n

        for i in range(n):
            acc += ones
            operations[i] = acc

            if boxes[i] == "1":
                ones += 1

        acc = 0
        ones = 0

        for i in range(n - 1, -1, -1):
            acc += ones
            operations[i] += acc

            if boxes[i] == "1":
                ones += 1

        return operations
