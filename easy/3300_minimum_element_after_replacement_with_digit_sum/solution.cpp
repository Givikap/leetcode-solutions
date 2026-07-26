#include <vector>

class Solution {
public:
  int minElement(std::vector<int> &nums) {
    int minReplacement = INT_MAX;

    for (int &num : nums) {
      int replacement = 0;

      while (num) {
        replacement += num % 10;
        num /= 10;
      }

      minReplacement = std::min(minReplacement, replacement);
    }

    return minReplacement;
  }
};
