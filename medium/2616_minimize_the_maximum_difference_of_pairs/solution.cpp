#include <algorithm>
#include <vector>

class Solution {
public:
  int minimizeMax(std::vector<int> &nums, int p) {
    std::sort(nums.begin(), nums.end());

    int left = 0;
    int right = nums.back() - nums.front();

    while (left < right) {
      int mid = (left + right) / 2;

      int count = 0;
      for (size_t i = 1; i < nums.size(); ++i) {
        if (nums[i] - nums[i - 1] <= mid) {
          ++count;
          ++i;
        }
      }

      if (count >= p)
        right = mid;
      else
        left = mid + 1;
    }

    return left;
  }
};
