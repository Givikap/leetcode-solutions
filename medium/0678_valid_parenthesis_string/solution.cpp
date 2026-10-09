#include <string>

class Solution {
public:
  bool checkValidString(std::string s) {
    const size_t n = s.size();

    int openCount = 0;
    int closeCount = 0;

    for (size_t i{}; i < n; ++i) {
      if (s[i] == '(' || s[i] == '*')
        ++openCount;
      else
        --openCount;

      if (s[n - i - 1] == ')' || s[n - i - 1] == '*')
        ++closeCount;
      else
        --closeCount;

      if (openCount < 0 || closeCount < 0)
        return false;
    }

    return true;
  }
};
