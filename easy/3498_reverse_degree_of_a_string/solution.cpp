#include <ranges>
#include <string>

class Solution {
public:
  int reverseDegree(std::string s) {
    int degree = 0;

    for (const auto &[i, ch] : s | std::views::enumerate)
      degree += ('{' - ch) * (i + 1);

    return degree;
  }
};
