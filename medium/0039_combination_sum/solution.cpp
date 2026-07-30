#include <algorithm>
#include <stack>
#include <tuple>
#include <vector>

class Solution {
public:
  std::vector<std::vector<int>> combinationSum(std::vector<int> &candidates,
                                               int target) {
    const size_t n = candidates.size();
    std::sort(candidates.begin(), candidates.end());

    std::vector<int> path;

    std::stack<std::tuple<size_t, int, bool>> s;
    s.push({0, target, false});

    std::vector<std::vector<int>> combinations;

    while (!s.empty()) {
      auto &[i, remaining, done] = s.top();

      if (!done) {
        if (remaining == 0) {
          combinations.push_back(path);
          s.pop();
        } else if (i == n || candidates[i] > remaining) {
          s.pop();
        } else {
          path.push_back(candidates[i]);
          done = true;
          s.push({i, remaining - candidates[i], 0});
        }
      } else {
        path.pop_back();
        s.pop();
        s.push({i + 1, remaining, 0});
      }
    }

    return combinations;
  }
};
