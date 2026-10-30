class Solution:
    def uniqueXorTriplets(self, nums: list[int]) -> int:
        n = len(nums)
        maxXor = 2048

        xorPairs = [False] * maxXor
        xorTriplets = [False] * maxXor

        for i in range(n):
            for j in range(i, n):
                xorPairs[nums[i] ^ nums[j]] = True

        for x in range(maxXor):
            if not xorPairs[x]:
                continue

            for num in nums:
                xorTriplets[x ^ num] = True

        return sum(1 for xorTriplet in xorTriplets if xorTriplet)
