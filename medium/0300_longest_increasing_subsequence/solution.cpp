#include <algorithm>
#include <vector>

class Solution {
public:
  int lengthOfLIS(std::vector<int> &nums) {
    std::vector<int> tails;

    for (const int &num : nums) {
      if (num > tails.back())
        tails.push_back(num);
      else if (num < tails.back())
        *lower_bound(tails.begin(), tails.end(), num) = num;
    }

    return static_cast<int>(tails.size());
  }
};
