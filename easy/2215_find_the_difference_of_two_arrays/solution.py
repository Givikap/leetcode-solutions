class Solution:
    def findDifference(
        self, nums1: list[int], nums2: list[int]
    ) -> list[list[int]]:
        nums1_set = set(nums1)
        nums2_set = set(nums2)

        answer = [[], []]

        for num in nums1_set:
            if num not in nums2_set:
                answer[0].append(num)

        for num in nums2_set:
            if num not in nums1_set:
                answer[1].append(num)

        return answer
