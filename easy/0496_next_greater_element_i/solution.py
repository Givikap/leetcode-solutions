class Solution:
    def nextGreaterElement(
        self, nums1: list[int], nums2: list[int]
    ) -> list[int]:
        next_greater_elements_map = {}

        for i in range(len(nums2) - 1):
            for j in range(i + 1, len(nums2)):
                if nums2[i] < nums2[j]:
                    next_greater_elements_map[nums2[i]] = nums2[j]
                    break

        return [next_greater_elements_map.get(num, -1) for num in nums1]
