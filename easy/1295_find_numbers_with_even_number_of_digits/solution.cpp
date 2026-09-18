#include <vector>

class Solution {
public:
  int findNumbers(std::vector<int> &nums) {
    auto countDigit = [](int num) {
      int digitCount = 0;

      while (num) {
        ++digitCount;
        num /= 10;
      }

      return digitCount;
    };

    int numCount = 0;

    for (const auto &num : nums) {
      if (countDigit(num) % 2 == 0)
        ++numCount;
    }

    return numCount;
  }
};
