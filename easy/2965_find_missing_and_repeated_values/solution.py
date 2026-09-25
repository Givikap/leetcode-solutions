class Solution:
    def findMissingAndRepeatedValues(self, grid: list[list[int]]) -> list[int]:
        answer = [0, 0]

        nums_set = set(range(1, len(grid) ** 2 + 1))

        for row in grid:
            for num in row:
                if num in nums_set:
                    nums_set.remove(num)
                else:
                    answer[0] = num

        answer[1] = nums_set.pop()
        return answer
