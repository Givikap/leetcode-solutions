#include <ranges>
#include <vector>

class Solution {
public:
  std::vector<int> shortestToChar(std::string s, char c) {
    std::vector<int> occurences;
    for (const auto &[i, ch] : s | std::views::enumerate) {
      if (ch == c)
        occurences.push_back(static_cast<int>(i));
    }

    size_t rightIdx = 0;

    int left = INT_MIN;
    int right = occurences[rightIdx];

    std::vector<int> distances(s.size());

    for (size_t i{}; i < s.size(); ++i) {
      distances[i] = std::min(i - left, right - i);

      if (distances[i] == 0) {
        left = right;
        right = ++rightIdx < occurences.size() ? occurences[rightIdx] : INT_MAX;
      }
    }

    return distances;
  }
};
