#include <vector>

class Solution {
public:
  int smallestRangeI(std::vector<int> &nums, int k) {
    int maxNum = nums[0];
    int minNum = maxNum;

    for (const auto &num : nums) {
      if (num > maxNum)
        maxNum = num;
      else if (num < minNum)
        minNum = num;
    }

    return std::max(maxNum - minNum - 2 * k, 0);
  }
};
