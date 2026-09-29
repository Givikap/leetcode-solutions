#include <stack>
#include <string>

class Solution {
public:
  std::string removeOuterParentheses(std::string s) {
    std::stack<char> st;
    std::string result;
    result.reserve(s.size());

    for (const auto &ch : s) {
      if (ch == '(') {
        if (!st.empty())
          result.push_back(ch);

        st.push(ch);
      } else {
        st.pop();

        if (!st.empty())
          result.push_back(ch);
      }
    }

    return result;
  }
};
