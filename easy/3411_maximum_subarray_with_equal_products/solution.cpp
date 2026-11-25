#include <numeric>
#include <vector>

class Solution {
public:
  int maxLength(std::vector<int> &nums) {
    size_t n = nums.size();

    size_t maxLen = 1;

    for (size_t i{}; i < n; ++i) {
      long long subarrayProduct = 1ll;
      long long subarrayGcd = 0ll;
      long long subarrayLcm = 1ll;

      for (size_t j = i; j < n; ++j) {
        subarrayProduct *= static_cast<size_t>(nums[j]);
        subarrayGcd = std::gcd(subarrayGcd, static_cast<size_t>(nums[j]));
        subarrayLcm = std::lcm(subarrayLcm, static_cast<size_t>(nums[j]));

        if (subarrayProduct == subarrayGcd * subarrayLcm)
          maxLen = std::max(maxLen, j - i + 1zu);
      }
    }

    return static_cast<size_t>(maxLen);
  }
};
