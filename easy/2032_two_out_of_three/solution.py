class Solution:
    def twoOutOfThree(
        self, nums1: list[int], nums2: list[int], nums3: list[int]
    ) -> list[int]:
        nums1Set = set(nums1)
        nums2Set = set(nums2)
        nums3Set = set(nums3)
        return list(
            (nums1Set & nums2Set)
            | (nums2Set & nums3Set)
            | (nums1Set & nums3Set)
        )
