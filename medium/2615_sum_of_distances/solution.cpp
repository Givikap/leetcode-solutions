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
      std::sort(indices.begin(), indices.end());

      size_t k = indices.size();

      std::vector<long long> prefixSums(k + 1, 0);
      for (size_t m = 1; m <= k; ++m)
        prefixSums[m] = prefixSums[m - 1] + indices[m - 1];

      for (size_t m{}; m < k; ++m) {
        long long index = indices[m];

        long long leftSum = index * static_cast<long long>(m) - prefixSums[m];
        long long rightSum = (prefixSums[k] - prefixSums[m] - index) -
                             index * static_cast<long long>(k - 1 - m);

        numsSums[index] = leftSum + rightSum;
      }
    }

    return numsSums;
  }
};
