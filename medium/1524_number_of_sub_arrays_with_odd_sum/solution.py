class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        evenCount = 1
        oddCount = 0

        prefixSum = 0

        count = 0

        for num in arr:
            prefixSum += num

            if prefixSum % 2 == 0:
                count += oddCount
                evenCount += 1
            else:
                count += evenCount
                oddCount += 1

        return count % (10**9 + 7)
