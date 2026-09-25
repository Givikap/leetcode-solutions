class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        if k == 0:
            return False

        visited = set()

        for i in range(min(k, len(nums))):
            if nums[i] in visited:
                return True

            visited.add(nums[i])

        for i in range(k, len(nums)):
            if nums[i] in visited:
                return True

            visited.add(nums[i])
            visited.remove(nums[i - k])

        return False
