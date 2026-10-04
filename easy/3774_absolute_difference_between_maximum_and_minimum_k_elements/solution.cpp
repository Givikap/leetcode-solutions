#include <algorithm>
#include <cstdlib>
#include <ranges>
#include <vector>

class Solution {
public:
  int absDifference(std::vector<int> &nums, int k) {
    std::ranges::sort(nums);
    return abs(
        std::ranges::fold_left(
            nums | std::views::take(static_cast<std::ptrdiff_t>(k)), 0,
            std::plus<>{}) -
        std::ranges::fold_left(
            nums |
                std::views::drop(static_cast<std::ptrdiff_t>(nums.size() - k)) |
                std::views::take(k),
            0, std::plus<>{}));
  }
};
