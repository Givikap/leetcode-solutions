#include <cstdlib>
#include <string>

class Solution {
public:
  int countValidPrefixes(std::string s) {
    int zerosCount = 0;
    int onesCount = 0;

    int validPrefixesCount = 0;

    for (const auto &ch : s) {
      if (ch == '0')
        ++zerosCount;
      else
        ++onesCount;

      if (abs(zerosCount - onesCount) < 2)
        ++validPrefixesCount;
    }

    return validPrefixesCount;
  }
};
