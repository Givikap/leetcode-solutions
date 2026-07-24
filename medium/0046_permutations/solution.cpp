#include <stack>
#include <vector>

class Solution {
public:
  std::vector<std::vector<int>> permute(std::vector<int> &nums) {
    std::vector<std::vector<int>> permutations;

    std::stack<std::pair<std::vector<int>, std::vector<bool>>> s;
    s.push({{}, std::vector<bool>(nums.size(), false)});

    while (!s.empty()) {
      std::vector<int> permutation = s.top().first;
      std::vector<bool> explored = s.top().second;
      s.pop();

      if (permutation.size() == nums.size()) {
        permutations.push_back(permutation);
      } else {
        for (size_t i{}; i < nums.size(); ++i) {
          if (explored[i])
            continue;

          std::vector<int> p(permutation);
          p.push_back(nums[i]);
          std::vector<bool> e(explored);
          e[i] = true;

          s.push({p, e});
        }
      }
    }

    return permutations;
  }
};
