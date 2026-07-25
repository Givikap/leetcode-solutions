from typing import List


class Solution:
    def findMedianSortedArrays(
        self, nums1: List[int], nums2: List[int]
    ) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)

        left = 0
        right = m

        while left <= right:
            cut1 = (left + right) // 2
            cut2 = (m + n) // 2 - cut1

            l1 = nums1[cut1 - 1] if cut1 != 0 else float("-inf")
            r1 = nums1[cut1] if cut1 != m else float("inf")
            l2 = nums2[cut2 - 1] if cut2 != 0 else float("-inf")
            r2 = nums2[cut2] if cut2 != n else float("inf")

            if r1 < l2:
                left = cut1 + 1
            elif l1 > r2:
                right = cut1 - 1
            else:
                if (m + n) % 2 == 0:
                    return (max(l1, l2) + min(r1, r2)) / 2
                else:
                    return min(r1, r2)

        return 0.0
