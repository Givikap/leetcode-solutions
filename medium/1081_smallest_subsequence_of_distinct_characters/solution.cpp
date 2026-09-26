#include <ranges>
#include <string>
#include <unordered_map>
#include <unordered_set>

class Solution {
public:
  std::string smallestSubsequence(std::string s) {
    std::unordered_map<char, size_t> lastIdx;
    for (const auto &[i, ch] : s | std::views::enumerate)
      lastIdx[ch] = i;

    std::unordered_set<char> subsequenceSet;
    std::string subsequence;

    for (const auto &[i, ch] : s | std::views::enumerate) {
      if (subsequenceSet.contains(ch))
        continue;

      while (!subsequence.empty() && ch < subsequence.back() &&
             i < lastIdx[subsequence.back()]) {
        subsequenceSet.erase(subsequence.back());
        subsequence.pop_back();
      }

      subsequence.push_back(ch);
      subsequenceSet.insert(ch);
    }

    return subsequence;
  }
};
