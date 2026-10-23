#include <string>
#include <unordered_set>

class Solution {
public:
  std::string toGoatLatin(std::string sentence) {
    const std::unordered_set<char> vowelsSet = {'a', 'e', 'i', 'o', 'u'};

    size_t wordStart = 0;
    size_t wordEnd = 0;

    int aCount = 1;

    do {
      wordEnd = sentence.find(' ', wordStart);
      if (wordEnd == std::string::npos)
        wordEnd = sentence.size();

      if (!vowelsSet.contains(tolower(sentence[wordStart]))) {
        sentence.insert(wordEnd, 1, sentence[wordStart]);
        sentence.erase(wordStart, 1);
      }

      sentence.insert(wordEnd, "ma");
      sentence.insert(wordEnd + 2, aCount, 'a');

      wordStart = wordEnd + 3 + aCount++;
    } while (wordStart < sentence.size());

    return sentence;
  }
};
