#include <stack>
#include <tuple>
#include <vector>

class Solution {
public:
  std::vector<std::vector<int>> combinationSum(std::vector<int> &candidates,
                                               int target) {
    const size_t n = candidates.size();
    std::sort(candidates.begin(), candidates.end());

    std::stack<std::tuple<size_t, int, std::vector<int>>> s;
    s.push({0, 0, {}});

    std::vector<std::vector<int>> combinations;

    while (!s.empty()) {
      auto [i, sum, combination] = s.top();
      s.pop();

      if (sum == target) {
        combinations.push_back(combination);
        continue;
      }

      for (size_t j = i; j < n; ++j) {
        if (sum + candidates[j] <= target) {
          std::vector<int> c(combination);
          c.push_back(candidates[j]);
          s.push({j, sum + candidates[j], c});
        }
      }
    }

    return combinations;
  }
};
