#include <vector>

class Solution {
public:
  int minimumSumSubarray(std::vector<int> &nums, int l, int r) {
    const size_t n = nums.size();

    int minSum = INT_MAX;

    for (size_t s = static_cast<size_t>(l); s <= static_cast<size_t>(r); ++s) {
      int currSum = 0;
      for (size_t i{}; i < n; ++i) {
        currSum += nums[i];

        if (i + 2 > s) {
          if (currSum > 0)
            minSum = std::min(minSum, currSum);

          currSum -= nums[i - s + 1];
        }
      }
    }

    return minSum != INT_MAX ? minSum : -1;
  }
};
