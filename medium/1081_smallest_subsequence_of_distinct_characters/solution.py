class Solution:
    def smallestSubsequence(self, s: str) -> str:
        lastIdx = {c: i for i, c in enumerate(s)}

        st = []
        stSet = set()

        for i, c in enumerate(s):
            if c in stSet:
                continue

            while st and c < st[-1] and i < lastIdx[st[-1]]:
                stSet.remove(st.pop())

            st.append(c)
            stSet.add(c)

        return "".join(st)
