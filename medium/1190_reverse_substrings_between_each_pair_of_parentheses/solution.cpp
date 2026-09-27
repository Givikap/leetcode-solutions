#include <algorithm>
#include <ranges>
#include <stack>
#include <string>

class Solution {
public:
  std::string reverseParentheses(std::string s) {
    std::stack<std::string::iterator> st;

    for (auto it = s.begin(); it != s.end(); ++it) {
      if (*it == '(') {
        st.push(it);
      } else if (*it == ')') {
        std::reverse(st.top(), it + 1);
        st.pop();
      }
    }

    s.erase(std::remove_if(s.begin(), s.end(),
                           [](const auto &c) { return c == '(' || c == ')'; }),
            s.end());

    return s;
  }
};
