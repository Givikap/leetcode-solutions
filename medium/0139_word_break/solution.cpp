#include <algorithm>
#include <string>
#include <unordered_set>
#include <vector>

class Solution {
public:
  bool wordBreak(std::string s, std::vector<std::string> &wordDict) {
    std::sort(wordDict.begin(), wordDict.end());

    std::vector<std::string> sequences = {s};
    std::unordered_set<std::string> explored;

    while (!sequences.empty()) {
      const std::string sequence = sequences.back();
      sequences.pop_back();

      if (sequence.size() == 0)
        return true;

      if (explored.find(sequence) != explored.end())
        continue;
      explored.insert(sequence);

      for (const std::string &word : wordDict) {
        if (sequence.ends_with(word))
          sequences.push_back(
              sequence.substr(0, sequence.size() - word.size()));
      }
    }

    return false;
  }
};
