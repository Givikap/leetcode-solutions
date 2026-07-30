#include <unordered_set>
#include <vector>

class Solution {
public:
  int longestConsecutive(std::vector<int> &nums) {
    std::unordered_set<int> numsSet(nums.begin(), nums.end());

    int maxLen = 0;

    for (int num : numsSet) {
      if (numsSet.find(num - 1) != numsSet.end())
        continue;

      int currLen = 1;

      while (numsSet.find(num + 1) != numsSet.end()) {
        ++num;
        ++currLen;
      }

      maxLen = std::max(maxLen, currLen);
    }

    return maxLen;
  }
};
