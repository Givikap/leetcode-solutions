#include <vector>

class Solution {
public:
  int minimumSumSubarray(std::vector<int> &nums, int l, int r) {
    const size_t n = nums.size();

    std::vector<int> prefixSums(n + 1zu, 0);
    for (size_t i{}; i < n; ++i)
      prefixSums[i + 1] = prefixSums[i] + nums[i];

    int minSum = INT_MAX;

    for (size_t s = static_cast<size_t>(l); s <= static_cast<size_t>(r); ++s) {
      for (size_t i{}; i < n - s + 1zu; ++i) {
        int currSum = prefixSums[i + s] - prefixSums[i];

        if (currSum > 0)
          minSum = std::min(minSum, currSum);
      }
    }

    return minSum != INT_MAX ? minSum : -1;
  }
};
