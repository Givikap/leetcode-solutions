class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        st = [0]

        for c in s:
            if c == "(":
                st.append(0)
            else:
                inner = st.pop()
                outer = st.pop()

                st.append(outer + max(2 * inner, 1))

        return st.pop()
