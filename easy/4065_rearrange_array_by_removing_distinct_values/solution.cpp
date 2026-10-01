#include <map>
#include <vector>

class Solution {
public:
  std::vector<int> rearrangeArray(std::vector<int> &nums) {
    std::map<int, int> numsCounter;
    for (const auto &num : nums)
      ++numsCounter[num];

    std::vector<int> ans;
    ans.reserve(nums.size());

    for (size_t i{}; i < nums.size();) {
      for (auto &[num, count] : numsCounter) {
        if (count > 0) {
          ++i;
          --count;
          ans.push_back(num);
        }
      }
    }

    return ans;
  }
};
