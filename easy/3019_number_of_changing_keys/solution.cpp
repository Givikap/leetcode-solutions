#include <string>

class Solution {
public:
  int countKeyChanges(std::string s) {
    int keyChanges = 0;

    for (size_t i = 1; i < s.size(); ++i) {
      if (tolower(s[i - 1]) != tolower(s[i]))
        ++keyChanges;
    }

    return keyChanges;
  }
};
