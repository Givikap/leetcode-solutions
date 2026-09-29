class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        st = []

        result = []

        for c in s:
            if c == "(":
                if st:
                    result.append(c)

                st.append(c)
            else:
                st.pop()

                if st:
                    result.append(c)

        return "".join(result)
