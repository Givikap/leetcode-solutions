#include <string>
#include <vector>

class Solution {
public:
  std::vector<int> maxDepthAfterSplit(std::string seq) {
    int currDepth = 0;
    std::vector<int> answer;

    for (const auto &ch : seq) {
      if (ch == '(')
        answer.push_back(++currDepth % 2);
      else
        answer.push_back(currDepth-- % 2);
    }

    return answer;
  }
};
