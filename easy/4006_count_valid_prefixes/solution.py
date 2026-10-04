class Solution:
    def countValidPrefixes(self, s: str) -> int:
        zerosCount = 0
        onesCount = 0

        validPrefixesCount = 0

        for ch in s:
            if ch == "0":
                zerosCount += 1
            else:
                onesCount += 1

            if abs(zerosCount - onesCount) < 2:
                validPrefixesCount += 1

        return validPrefixesCount
