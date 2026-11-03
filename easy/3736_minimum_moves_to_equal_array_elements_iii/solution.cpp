#include <algorithm>
#include <ranges>
#include <vector>

class Solution {
public:
  int minMoves(std::vector<int> &nums) {
    const int maxNum = *std::ranges::max_element(nums);

    int movesCount = 0;
    for (const auto &num : nums)
      movesCount += maxNum - num;

    return movesCount;
  }
};
