class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums1.sort()
        nums2.sort()

        i1 = i2 = 0

        intersection = []

        while True:
            if i1 == len(nums1) or i2 == len(nums2):
                break

            if nums1[i1] == nums2[i2]:
                intersection.append(nums1[i1])
                i1 += 1
                i2 += 1
            elif nums1[i1] < nums2[i2]:
                i1 += 1
            else:
                i2 += 1

        return intersection
