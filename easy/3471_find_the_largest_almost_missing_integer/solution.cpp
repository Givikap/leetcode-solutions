#include <unordered_map>
#include <vector>

class Solution {
public:
  int largestInteger(std::vector<int> &nums, int k) {
    if (k == static_cast<int>(nums.size()))
      return *max_element(nums.begin(), nums.end());

    std::unordered_map<int, int> numsCounter;
    for (const int &num : nums)
      ++numsCounter[num];

    if (k == 1) {
      int maxNum = -1;

      for (const auto &[num, count] : numsCounter) {
        if (count == 1)
          maxNum = std::max(maxNum, num);
      }

      return maxNum;
    }

    if (numsCounter[nums[0]] == 1 && numsCounter[nums.back()] == 1)
      return (nums[0] > nums.back()) ? nums[0] : nums.back();
    else if (numsCounter[nums[0]] == 1)
      return nums[0];
    else if (numsCounter[nums.back()] == 1)
      return nums.back();

    return -1;
  }
};
