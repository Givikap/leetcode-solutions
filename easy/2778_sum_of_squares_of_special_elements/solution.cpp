#include <algorithm>
#include <ranges>
#include <vector>

class Solution {
public:
  int sumOfSquares(std::vector<int> &nums) {
    const size_t n = nums.size();
    size_t i = 1;

    return std::ranges::fold_left(nums, 0, [&](auto acc, const auto &num) {
      return acc + (n % i++ == 0 ? num * num : 0);
    });
  }
};
