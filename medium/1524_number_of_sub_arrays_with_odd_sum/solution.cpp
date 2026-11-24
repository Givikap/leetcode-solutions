#include <vector>

class Solution {
public:
  int numOfSubarrays(std::vector<int> &arr) {
    const int MOD = 1e9 + 7;

    int evenCount = 1;
    int oddCount = 0;

    int prefixSum = 0;

    int count = 0;

    for (const auto &num : arr) {
      prefixSum += num;

      if (prefixSum % 2 == 0) {
        count += oddCount;
        ++evenCount;
      } else {
        count += evenCount;
        ++oddCount;
      }

      count %= MOD;
    }

    return count;
  }
};
