#include <algorithm>
#include <ranges>
#include <vector>

class Solution {
public:
  std::vector<bool> kidsWithCandies(std::vector<int> &candies,
                                    int extraCandies) {
    const int maxCandies = *std::ranges::max_element(candies);

    std::vector<bool> result(candies.size());

    for (const auto &[i, candy] : candies | std::views::enumerate)
      result[i] = candy + extraCandies >= maxCandies;

    return result;
  }
};
