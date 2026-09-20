#include <list>
#include <vector>

class Solution {
public:
  std::vector<int> createTargetArray(std::vector<int> &nums,
                                     std::vector<int> &index) {
    const size_t n = nums.size();

    std::list<int> numsList;

    for (size_t i{}; i < n; ++i)
      numsList.insert(next(numsList.begin(), index[i]), nums[i]);

    std::vector<int> target;
    target.reserve(n);

    for (const auto &num : numsList)
      target.push_back(num);

    return target;
  }
};
