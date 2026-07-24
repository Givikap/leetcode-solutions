#include <vector>

class Solution {
public:
  std::vector<std::vector<int>> subsets(std::vector<int> &nums) {
    std::vector<std::vector<int>> subsets{{}};

    for (size_t i{}; i < nums.size(); ++i) {
      subsets.push_back({nums[i]});

      size_t limit = subsets.size() - 1;
      for (size_t j = 1; j < limit; ++j) {
        std::vector<int> subset{subsets[j]};
        subset.insert(subset.end(), subsets[limit].begin(),
                      subsets[limit].end());
        subsets.push_back(subset);
      }
    }

    return subsets;
  }
};
