#include <stack>
#include <string>

class Solution {
public:
  std::string removeOuterParentheses(std::string s) {
    std::stack<char> st;
    std::string result;

    for (const auto &ch : s) {
      if (!st.empty())
        result.push_back(ch);

      if (ch == '(')
        st.push(ch);
      else
        st.pop();

      if (st.empty())
        result.pop_back();
    }

    return result;
  }
};
