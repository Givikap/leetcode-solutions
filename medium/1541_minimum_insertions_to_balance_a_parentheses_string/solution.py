class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        st = []

        insertions = 0

        i = 0
        while i < n:
            if s[i] == "(":
                st.append("(")
            else:
                if i < n - 1 and s[i + 1] == ")":
                    i += 1
                else:
                    insertions += 1

                if st:
                    st.pop()
                else:
                    insertions += 1

            i += 1

        return insertions + len(st) * 2
