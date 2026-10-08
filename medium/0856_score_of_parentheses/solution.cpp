#include <stack>
#include <string>

class Solution {
public:
  int scoreOfParentheses(std::string s) {
    std::stack<int> st;
    st.push(0);

    for (const auto &ch : s) {
      if (ch == '(') {
        st.push(0);
      } else {
        int inner = st.top();
        st.pop();
        int outer = st.top();
        st.pop();

        st.push(outer + std::max(2 * inner, 1));
      }
    }

    return st.top();
  }
};
