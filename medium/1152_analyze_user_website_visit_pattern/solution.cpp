#include <algorithm>
#include <numeric>
#include <ranges>
#include <unordered_map>
#include <unordered_set>
#include <vector>

class Solution {
public:
  std::vector<std::string>
  mostVisitedPattern(std::vector<std::string> &username,
                     std::vector<int> &timestamp,
                     std::vector<std::string> &website) {
    std::vector<size_t> indices(timestamp.size());
    std::iota(indices.begin(), indices.end(), 0);

    std::sort(indices.begin(), indices.end(),
              [&](size_t i, size_t j) { return timestamp[i] < timestamp[j]; });

    std::unordered_map<std::string, std::vector<std::string>> visitsMap;

    for (const auto &i : indices)
      visitsMap[username[i]].push_back(website[i]);

    std::unordered_map<std::string, int> patternsCounter;

    for (const auto &[_, visits] : visitsMap) {
      const size_t n = visits.size();
      if (n < 3)
        continue;

      std::vector<bool> mask(3, false);
      mask.resize(n, true);

      std::unordered_set<std::string> patterns;

      do {
        std::vector<std::string> pattern;

        for (size_t i{}; i < n; ++i) {
          if (!mask[i])
            pattern.push_back(visits[i]);
        }

        patterns.insert(pattern | std::views::join_with('-') |
                        std::ranges::to<std::string>());
      } while (next_permutation(mask.begin(), mask.end()));

      for (const auto &pattern : patterns)
        ++patternsCounter[pattern];
    }

    return max_element(patternsCounter.begin(), patternsCounter.end(),
                       [](const auto &p1, const auto &p2) {
                         if (p1.second == p2.second)
                           return p1.first > p2.first;
                         return p1.second < p2.second;
                       })
               ->first |
           std::views::split('-') | std::ranges::to<std::vector<std::string>>();
  }
};
