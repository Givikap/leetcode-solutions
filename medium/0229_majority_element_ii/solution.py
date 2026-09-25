class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        m1, m2 = None, None
        c1, c2 = 0, 0

        for num in nums:
            if num == m1:
                c1 += 1
            elif num == m2:
                c2 += 1
            elif c1 == 0:
                m1 = num
                c1 = 1
            elif c2 == 0:
                m2 = num
                c2 = 1
            else:
                c1 -= 1
                c2 -= 1

        majorities = []

        if nums.count(m1) > len(nums) // 3:
            majorities.append(m1)
        if m2 is not None and nums.count(m2) > len(nums) // 3:
            majorities.append(m2)

        return majorities
