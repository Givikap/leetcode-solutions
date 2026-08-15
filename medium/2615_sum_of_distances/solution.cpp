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
      size_t k = indices.size();

      long long indicesSum = 0;
      for (const int &index : indices)
        indicesSum += index;

      long long leftSum = 0;

      for (size_t m{}; m < k; ++m) {
        long long rightSum = indicesSum - leftSum - indices[m];
        numsSums[indices[m]] = indices[m] * static_cast<long long>(m) -
                               leftSum + rightSum -
                               indices[m] * static_cast<long long>(k - m - 1);
        leftSum += indices[m];
      }
    }

    return numsSums;
  }
};
