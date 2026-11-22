#include <string>

class Solution {
public:
  bool checkString(std::string s) {
    bool seenB = false;

    for (const auto &ch : s) {
      if (ch == 'a' && seenB)
        return false;
      else if (ch == 'b')
        seenB = true;
    }

    return true;
  }
};
