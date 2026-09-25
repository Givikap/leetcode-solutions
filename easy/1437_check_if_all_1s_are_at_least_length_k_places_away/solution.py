class Solution:
    def kLengthApart(self, nums: list[int], k: int) -> bool:
        zeros_count = 1000001

        for num in nums:
            if num == 1:
                if zeros_count < k:
                    return False

                zeros_count = 0
            else:
                zeros_count += 1

        return True
