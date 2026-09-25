class Solution:
    def sequentialDigits(self, low: int, high: int) -> list[int]:
        digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        sequentialNums = []

        for count in range(1, 10):
            for i in range(len(digits)):
                if i == 10 - count:
                    break

                sequentialNum = 0

                for j in range(count):
                    sequentialNum = sequentialNum * 10 + digits[i + j]

                if low <= sequentialNum <= high:
                    sequentialNums.append(sequentialNum)

        return sequentialNums
