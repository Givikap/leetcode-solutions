class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        st = []
        parenthesesCount = 0

        for c in s:
            if c == "(":
                st.append("(")
            else:
                if st:
                    st.pop()
                else:
                    parenthesesCount += 1

        return parenthesesCount + len(st)
