#include <unordered_map>
#include <vector>

class Solution {
public:
  long long countBadPairs(std::vector<int> &nums) {
    const size_t n = nums.size();

    std::unordered_map<int, int> pairsMap;

    const long long pairsCount = n * (n - 1) / 2;
    long long goodPairsCount = 0;

    for (size_t i{}; i < n; ++i) {
      goodPairsCount += pairsMap[i - nums[i]]++;
    }

    return pairsCount - goodPairsCount;
  }
};
