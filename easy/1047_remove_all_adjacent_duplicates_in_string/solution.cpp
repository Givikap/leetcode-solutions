#include <stack>
#include <string>

class Solution {
public:
  std::string removeDuplicates(std::string s) {
    std::stack<char> st;

    for (const auto &ch : s) {
      if (!st.empty() && st.top() == ch)
        st.pop();
      else
        st.push(ch);
    }

    s.resize(st.size());

    for (size_t i = st.size() - 1; i != -1; --i) {
      s[i] = st.top();
      st.pop();
    }

    return s;
  }
};
