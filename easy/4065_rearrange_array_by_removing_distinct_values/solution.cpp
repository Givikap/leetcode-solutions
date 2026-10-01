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

    auto it = numsCounter.begin();

    while (!numsCounter.empty()) {
      while (it != numsCounter.end()) {
        if (it->second == 0) {
          it = numsCounter.erase(it);
        } else {
          --it->second;
          ans.push_back(it->first);
          ++it;
        }
      }

      it = numsCounter.begin();
    }

    return ans;
  }
};
