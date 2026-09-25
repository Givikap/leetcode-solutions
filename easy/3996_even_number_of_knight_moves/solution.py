class Solution:
    def canReach(self, start: list[int], target: list[int]) -> bool:
        return abs(target[0] - start[0]) % 2 == abs(target[1] - start[1]) % 2
