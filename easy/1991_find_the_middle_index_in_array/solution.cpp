#include <algorithm>
#include <vector>

class Solution {
public:
  int findMiddleIndex(std::vector<int> &nums) {
    int leftSum = 0;
    int rightSum = std::ranges::fold_left(nums, 0, std::plus<int>());

    for (size_t mid{}; mid < nums.size(); ++mid) {
      rightSum -= nums[mid];

      if (leftSum == rightSum)
        return static_cast<int>(mid);

      leftSum += nums[mid];
    }

    return -1;
  }
};
