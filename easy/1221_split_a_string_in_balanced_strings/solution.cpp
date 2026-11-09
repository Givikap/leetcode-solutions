#include <string>

class Solution {
public:
  int balancedStringSplit(std::string s) {
    int balance = 0;
    int count = 0;

    for (const auto &ch : s) {
      if (ch == 'L')
        ++balance;
      else
        --balance;

      if (balance == 0)
        ++count;
    }

    return count;
  }
};
