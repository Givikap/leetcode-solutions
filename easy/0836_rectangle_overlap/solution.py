from typing import List


class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x11, y11, x12, y12 = rec1
        x21, y21, x22, y22 = rec2

        return not (x11 >= x22 or x12 <= x21 or y11 >= y22 or y12 <= y21)
