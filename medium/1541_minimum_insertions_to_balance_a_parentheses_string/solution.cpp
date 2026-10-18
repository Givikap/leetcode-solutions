#include <string>

class Solution {
public:
  int minInsertions(std::string s) {
    const size_t n = s.size();

    int openCount = 0;
    int insertions = 0;

    for (size_t i{}; i < n; ++i) {
      if (s[i] == '(') {
        ++openCount;
      } else {
        if (i < n - 1 && s[i + 1] == ')')
          ++i;
        else
          ++insertions;

        if (openCount == 0)
          ++insertions;
        else
          --openCount;
      }
    }

    return insertions + 2 * openCount;
  }
};
