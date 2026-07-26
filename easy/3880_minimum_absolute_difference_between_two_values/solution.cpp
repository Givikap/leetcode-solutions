#include <vector>

class Solution {
public:
  int minAbsoluteDifference(std::vector<int> &nums) {
    int minDifference = INT_MAX;

    int prevNum = 0;
    int prevI = 0;

    for (int i = 0; i < nums.size(); ++i) {
      if (nums[i] == 0)
        continue;

      if (prevNum == 3 - nums[i] && i - prevI < minDifference)
        minDifference = i - prevI;

      prevNum = nums[i];
      prevI = i;
    }

    return minDifference != INT_MAX ? minDifference : -1;
  }
};
