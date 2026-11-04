#include <algorithm>
#include <cstdlib>
#include <ranges>
#include <vector>

class Solution {
public:
  int minMoves2(std::vector<int> &nums) {
    const size_t n = nums.size();
    const size_t mid = n / 2;

    std::ranges::nth_element(nums, nums.begin() + mid);

    int median;
    if (n % 2 == 0) {
      auto it = std::max_element(nums.begin(), nums.begin() + mid);
      median = static_cast<int>(static_cast<double>(nums[mid] + *it) / 2.0);
    } else {
      median = nums[mid];
    }

    int movesCount = 0;
    for (const auto &num : nums)
      movesCount += std::abs(num - median);

    return movesCount;
  }
};
