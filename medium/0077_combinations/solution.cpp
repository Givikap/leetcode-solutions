#include <vector>

class Solution {
public:
  std::vector<std::vector<int>> combine(int n, int k) {
    std::vector<int> combination;
    std::vector<std::vector<int>> combinations;

    auto backtrack = [&](this const auto &self, int start) -> void {
      if (combination.size() == static_cast<size_t>(k)) {
        combinations.push_back(std::vector<int>(combination));
        return;
      }

      for (int num = start; num < n + 1; ++num) {
        combination.push_back(num);
        self(num + 1);
        combination.pop_back();
      }
    };

    backtrack(1);
    return combinations;
  }
};
