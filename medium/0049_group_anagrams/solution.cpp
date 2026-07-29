#include <array>
#include <map>
#include <string>
#include <vector>

class Solution {
public:
  std::vector<std::vector<std::string>>
  groupAnagrams(std::vector<std::string> &strs) {
    std::map<std::array<int, 26>, std::vector<std::string>> anagramsMap;

    for (const std::string &str : strs) {
      std::array<int, 26> charCounter{};
      for (const char &ch : str)
        ++charCounter[ch - 'a'];

      anagramsMap[charCounter].push_back(str);
    }

    std::vector<std::vector<std::string>> anagramGroups;
    anagramGroups.reserve(anagramsMap.size());

    for (const auto &[_, anagrams] : anagramsMap)
      anagramGroups.push_back(std::move(anagrams));

    return anagramGroups;
  }
};
