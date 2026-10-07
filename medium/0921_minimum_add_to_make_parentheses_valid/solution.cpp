#include <string>

class Solution {
public:
  int minAddToMakeValid(std::string s) {
    int openParenthesesCount = 0;
    int missingParenthesesCount = 0;

    for (const auto &ch : s) {
      if (ch == '(') {
        ++openParenthesesCount;
      } else {
        if (openParenthesesCount > 0)
          --openParenthesesCount;
        else
          ++missingParenthesesCount;
      }
    }

    return openParenthesesCount + missingParenthesesCount;
  }
};
