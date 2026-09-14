#include <algorithm>
class Solution {
public:
  long long countCommas(long long n) {
    long long commasCount = 0;

    for (long long bound = 1000, multiplier = 1; bound <= n;
         bound *= 1000, ++multiplier)
      commasCount += (std::min(bound * 1000 - 1, n) - bound + 1) * multiplier;

    return commasCount;
  }
};
