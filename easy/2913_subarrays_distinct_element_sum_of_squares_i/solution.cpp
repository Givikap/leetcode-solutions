#include <array>
#include <vector>

class Solution {
public:
  int sumCounts(std::vector<int> &nums) {
    const size_t n = nums.size();

    int countSquaresSum = 0;

    for (size_t i{}; i < n; ++i) {
      std::array<bool, 101> seen;
      seen.fill(false);

      int distinctCount = 0;

      for (size_t j = i; j < n; ++j) {
        if (!seen[static_cast<size_t>(nums[j])]) {
          seen[static_cast<size_t>(nums[j])] = true;
          ++distinctCount;
        }

        countSquaresSum += distinctCount * distinctCount;
      }
    }

    return countSquaresSum;
  }
};
