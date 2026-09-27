class Solution:
    def reverseParentheses(self, s: str) -> str:
        st = []
        sList = list(s)

        for i, c in enumerate(s):
            if c == "(":
                st.append(i)
            elif c == ")":
                start = st.pop()
                end = i + 1

                sList[start:end] = sList[start:end][::-1]

        return "".join(c for c in sList if c not in ("(", ")"))
