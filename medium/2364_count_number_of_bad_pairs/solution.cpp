#include <unordered_map>
#include <vector>

class Solution {
public:
  long long countBadPairs(std::vector<int> &nums) {
    const size_t n = nums.size();

    std::unordered_map<int, int> pairsMap;
    for (size_t i{}; i < n; ++i)
      ++pairsMap[i - nums[i]];

    long long goodPairsCount = 0;

    for (const auto &[diff, count] : pairsMap)
      goodPairsCount += static_cast<long long>(count) * (count - 1) / 2;

    return (n * (n - 1) / 2) - goodPairsCount;
  }
};
