class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        currDepth = 0
        answer = []

        for c in seq:
            if c == "(":
                currDepth += 1
                answer.append(currDepth % 2)
            else:
                answer.append(currDepth % 2)
                currDepth -= 1

        return answer
