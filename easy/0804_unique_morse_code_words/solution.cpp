#include <string>
#include <unordered_set>
#include <vector>

class Solution {
public:
  int uniqueMorseRepresentations(std::vector<std::string> &words) {
    const std::vector<std::string> morseMap = {
        ".-",   "-...", "-.-.", "-..",  ".",   "..-.", "--.",  "....", "..",
        ".---", "-.-",  ".-..", "--",   "-.",  "---",  ".--.", "--.-", ".-.",
        "...",  "-",    "..-",  "...-", ".--", "-..-", "-.--", "--.."};
    std::unordered_set<std::string> morseCodesSet;

    for (const auto &word : words) {
      std::string morseCode;

      for (const auto &ch : word)
        morseCode += morseMap[ch - 'a'];

      morseCodesSet.insert(morseCode);
    }

    return static_cast<int>(morseCodesSet.size());
  }
};
