class Solution:
    def minimumBoxes(self, apples: list[int], boxes: list[int]) -> int:
        apples_count = sum(apples)
        boxes_count = 0

        for box in sorted(boxes, reverse=True):
            apples_count -= box
            boxes_count += 1

            if apples_count <= 0:
                return boxes_count
