class Solution:
    def merge(
        self, nums1: list[int], m: int, nums2: list[int], n: int
    ) -> None:
        if not nums2:
            return

        i1 = m - 1
        i2 = n - 1

        for i in range(m + n - 1, -1, -1):
            if i2 < 0:
                break
            elif i1 >= 0 and nums1[i1] >= nums2[i2]:
                nums1[i] = nums1[i1]
                i1 -= 1
            else:
                nums1[i] = nums2[i2]
                i2 -= 1
