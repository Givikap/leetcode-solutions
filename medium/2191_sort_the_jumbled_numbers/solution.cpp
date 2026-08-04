#include <vector>

class Solution {
public:
  std::vector<int> sortJumbled(std::vector<int> &mapping,
                               std::vector<int> &nums) {
    auto mapJumbled = [&](int num) {
      if (num == 0)
        return mapping[0];

      int mul = 1;
      int jumbledNum = 0;

      while (num) {
        jumbledNum += mapping[num % 10] * mul;
        num /= 10;
        mul *= 10;
      }

      return jumbledNum;
    };

    std::stable_sort(nums.begin(), nums.end(), [&](const int &a, const int &b) {
      return mapJumbled(a) < mapJumbled(b);
    });

    return nums;
  }
};
