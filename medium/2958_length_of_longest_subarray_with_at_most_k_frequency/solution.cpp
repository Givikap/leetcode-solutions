#include <unordered_map>
#include <vector>

class Solution {
public:
  int maxSubarrayLength(std::vector<int> &nums, int k) {
    std::unordered_map<int, int> numsCounter;

    size_t left = 0;
    size_t right = 0;

    size_t maxLen = 0;

    for (size_t left{}, right{}; right < nums.size();) {
      int num = nums[right];

      if (numsCounter[num] < k) {
        ++numsCounter[num];
        ++right;
      } else {
        while (numsCounter[num] == k)
          --numsCounter[nums[left++]];
      }

      maxLen = std::max(maxLen, right - left);
    }

    return static_cast<int>(maxLen);
  }
};
