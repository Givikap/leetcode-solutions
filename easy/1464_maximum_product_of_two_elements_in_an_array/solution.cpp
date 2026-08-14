#include <vector>

class Solution {
public:
  int maxProduct(std::vector<int> &nums) {
    int secondMaxNum = -1;
    int maxNum = 0;

    for (const int &num : nums) {
      if (num > maxNum) {
        secondMaxNum = maxNum;
        maxNum = num;
      } else if (num > secondMaxNum) {
        secondMaxNum = num;
      }
    }

    return (secondMaxNum - 1) * (maxNum - 1);
  }
};
