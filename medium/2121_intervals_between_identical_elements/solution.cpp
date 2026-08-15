#include <unordered_map>
#include <vector>

class Solution {
public:
  std::vector<long long> getDistances(std::vector<int> &arr) {
    const size_t n = arr.size();

    std::unordered_map<int, std::vector<long long>> indicesMap;
    for (size_t i{}; i < n; ++i)
      indicesMap[arr[i]].push_back(static_cast<long long>(i));

    std::vector<long long> numsSums(n);

    for (auto &[_, indices] : indicesMap) {
      size_t k = indices.size();

      long long indicesSum = 0;
      for (const int &index : indices)
        indicesSum += index;

      long long leftSum = 0;

      for (size_t m{}; m < k; ++m) {
        long long index = indices[m];
        numsSums[index] = indicesSum - 2 * leftSum -
                          index * static_cast<long long>(k - 2 * m);
        leftSum += index;
      }
    }

    return numsSums;
  }
};
