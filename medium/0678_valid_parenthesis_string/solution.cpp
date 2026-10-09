#include <string>

class Solution {
public:
  bool checkValidString(std::string s) {
    int openCount = 0;
    int closeCount = 0;

    for (size_t left = 0, right = s.size() - 1; right != -1; ++left, --right) {
      if (s[left] == '(' || s[left] == '*')
        ++openCount;
      else
        --openCount;

      if (s[right] == ')' || s[right] == '*')
        ++closeCount;
      else
        --closeCount;

      if (openCount < 0 || closeCount < 0)
        return false;
    }

    return true;
  }
};
