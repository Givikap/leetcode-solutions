#include <vector>

class Solution {
public:
  int minMoves(std::vector<int> &nums) {
    int maxNum = 0;
    int numsSum = 0;

    for (const auto &num : nums) {
      maxNum = std::max(maxNum, num);
      numsSum += num;
    }

    return maxNum * static_cast<int>(nums.size()) - numsSum;
  }
};
