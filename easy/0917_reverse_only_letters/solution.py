class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        slist = list(s)

        left = 0
        right = len(slist) - 1

        while left < right:
            if slist[left].isalpha() and slist[right].isalpha():
                slist[left], slist[right] = slist[right], slist[left]
                left += 1
                right -= 1
            elif slist[left].isalpha():
                right -= 1
            else:
                left += 1

        return "".join(slist)
