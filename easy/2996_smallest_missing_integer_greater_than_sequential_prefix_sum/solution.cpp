#include <unordered_set>
#include <vector>

class Solution {
public:
  int missingInteger(std::vector<int> &nums) {
    const size_t n = nums.size();

    int sequentialPrefixSum = nums[0];
    std::unordered_set<int> numsSet = {nums[0]};

    size_t i = 1;
    for (; i < n && nums[i - 1] + 1 == nums[i]; ++i) {
      sequentialPrefixSum += nums[i];
      numsSet.insert(nums[i]);
    }

    for (; i < n; ++i)
      numsSet.insert(nums[i]);

    while (numsSet.find(sequentialPrefixSum) != numsSet.end())
      ++sequentialPrefixSum;

    return sequentialPrefixSum;
  }
};
