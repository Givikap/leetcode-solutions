class Solution:
    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:
        n1 = len(nums1)
        n2 = len(nums2)

        i1 = 0
        i2 = 0

        while i1 < n1 and i2 < n2:
            num1 = nums1[i1]
            num2 = nums2[i2]

            if num1 == num2:
                return num1
            elif num1 < num2:
                i1 += 1
            else:
                i2 += 1

        return -1
