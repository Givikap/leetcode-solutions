class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        dividingNums = []

        for num in range(left, right + 1):
            numCopy = num
            while numCopy:
                digit = numCopy % 10

                if digit == 0 or num % digit != 0:
                    break

                numCopy //= 10

            if numCopy == 0:
                dividingNums.append(num)

        return dividingNums
