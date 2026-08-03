#include <unordered_map>
#include <vector>

class Solution {
public:
  int countNicePairs(std::vector<int> &nums) {
    std::unordered_map<int, long long> pairsMap;

    for (const int &num : nums) {
      int numCopy = num;
      int numReversed = 0;

      while (numCopy) {
        numReversed = numReversed * 10 + numCopy % 10;
        numCopy /= 10;
      }

      ++pairsMap[num - numReversed];
    }

    const long long MOD = 1'000'000'007;
    long long nicePairsCount = 0;

    for (const auto &[_, count] : pairsMap)
      nicePairsCount = (nicePairsCount + count * (count - 1) / 2) % MOD;

    return static_cast<int>(nicePairsCount);
  }
};
