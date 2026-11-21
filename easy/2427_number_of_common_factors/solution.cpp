#include <algorithm>

class Solution {
public:
  int commonFactors(int a, int b) {
    int count = 1;

    for (int factor = std::min(a, b); factor > 1; --factor) {
      if (a % factor == 0 && b % factor == 0)
        ++count;
    }

    return count;
  }
};
