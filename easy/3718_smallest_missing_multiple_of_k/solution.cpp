#include <unordered_set>
#include <vector>

class Solution {
public:
  int missingMultiple(std::vector<int> &nums, int k) {
    std::unordered_set<int> numsSet(nums.begin(), nums.end());

    int m = k;
    for (; numsSet.find(m) != numsSet.end(); m += k)
      ;

    return m;
  }
};
