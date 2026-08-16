#include <vector>

class Solution {
public:
  int findLengthOfLCIS(std::vector<int> &nums) {
    const size_t n = nums.size();

    int maxLen = 1;

    for (size_t i = 1; i < n; ++i) {
      int currLen = 1;

      while (i < n && nums[i - 1] < nums[i]) {
        ++currLen;
        ++i;
      }

      maxLen = std::max(maxLen, currLen);
    }

    return maxLen;
  }
};
