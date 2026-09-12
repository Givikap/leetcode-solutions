class Solution:
    def customSortString(self, order: str, s: str) -> str:
        orderMap = {}

        for i, ch in enumerate(order):
            orderMap[ch] = i

        return "".join(sorted(s, key=lambda ch: orderMap.get(ch, 26)))
