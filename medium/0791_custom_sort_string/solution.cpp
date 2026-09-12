#include <algorithm>
#include <ranges>
#include <string>
#include <vector>

class Solution {
public:
  std::string customSortString(std::string order, std::string s) {
    std::vector<size_t> orderMap(26, 26);
    for (size_t i{}; i < order.size(); ++i)
      orderMap[static_cast<size_t>(order[i] - 'a')] = i;

    std::ranges::sort(s, [&](const auto &ch1, const auto &ch2) {
      return orderMap[static_cast<size_t>(ch1 - 'a')] <
             orderMap[static_cast<size_t>(ch2 - 'a')];
    });

    return s;
  }
};
