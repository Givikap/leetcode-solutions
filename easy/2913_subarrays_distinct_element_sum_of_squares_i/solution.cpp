#include <unordered_map>
#include <vector>

class Solution {
public:
  int sumCounts(std::vector<int> &nums) {
    const size_t n = nums.size();

    int countSquaresSum = static_cast<int>(n);

    for (size_t s = 2; s <= n; ++s) {
      std::unordered_map<int, int> subarrayCounter;
      for (size_t i{}; i < s; ++i)
        ++subarrayCounter[nums[i]];

      countSquaresSum +=
          static_cast<int>(subarrayCounter.size()) * subarrayCounter.size();

      for (size_t j = s; j < n; ++j) {
        --subarrayCounter[nums[j - s]];
        if (subarrayCounter[nums[j - s]] == 0)
          subarrayCounter.erase(nums[j - s]);
        ++subarrayCounter[nums[j]];

        countSquaresSum +=
            static_cast<int>(subarrayCounter.size()) * subarrayCounter.size();
      }
    }

    return countSquaresSum;
  }
};
