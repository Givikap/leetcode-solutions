#include <string>
#include <unordered_map>
#include <vector>

class Solution {
public:
  std::vector<std::vector<std::string>>
  groupAnagrams(std::vector<std::string> &strs) {
    std::unordered_map<std::string, std::vector<std::string>> anagramsMap;

    for (const std::string &str : strs) {
      std::string hash(str);
      std::sort(hash.begin(), hash.end());
      anagramsMap[hash].push_back(str);
    }

    std::vector<std::vector<std::string>> anagramGroups;
    anagramGroups.reserve(anagramsMap.size());

    for (const auto &[_, anagrams] : anagramsMap)
      anagramGroups.push_back(std::move(anagrams));

    return anagramGroups;
  }
};
