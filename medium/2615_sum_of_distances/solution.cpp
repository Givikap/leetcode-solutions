#include <algorithm>
#include <unordered_map>
#include <vector>

class Solution {
public:
  std::vector<long long> distance(std::vector<int> &nums) {
    const size_t n = nums.size();

    std::unordered_map<int, std::vector<long long>> indicesMap;

    for (size_t i{}; i < n; ++i)
      indicesMap[nums[i]].push_back(static_cast<long long>(i));

    std::vector<long long> numsSums(n, 0);

    for (auto &[_, indices] : indicesMap) {
      sort(indices.begin(), indices.end());

      size_t k = indices.size();

      std::vector<long long> prefixSums(k + 1, 0);
      for (size_t m = 1; m < k + 1; ++m)
        prefixSums[m] = prefixSums[m - 1] + indices[m - 1];

      for (size_t m{}; m < k; ++m)
        numsSums[indices[m]] = prefixSums[k] - 2 * prefixSums[m] -
                               indices[m] * static_cast<long long>(k - 2 * m);
    }

    return numsSums;
  }
};
