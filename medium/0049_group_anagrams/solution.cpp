#include <map>
#include <string>
#include <vector>

class Solution {
public:
  std::vector<std::vector<std::string>>
  groupAnagrams(std::vector<std::string> &strs) {
    std::map<std::vector<int>, std::vector<std::string>> anagramsMap;

    for (const std::string &str : strs) {
      std::vector<int> charCounter(26, 0);
      for (const char &ch : str)
        ++charCounter[ch - 'a'];

      anagramsMap[charCounter].push_back(str);
    }

    std::vector<std::vector<std::string>> anagramGroups;
    for (const auto &[_, anagrams] : anagramsMap)
      anagramGroups.push_back(anagrams);

    return anagramGroups;
  }
};
