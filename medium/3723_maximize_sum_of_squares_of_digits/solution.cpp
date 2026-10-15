#include <cstdlib>
#include <string>

class Solution {
public:
  std::string maxSumOfSquares(int num, int sum) {
    if (sum > 9 * num)
      return "";

    auto result = div(sum, 9);
    int q = result.quot;
    int r = result.rem;

    std::string ans(q, '9');
    if (r > 0)
      ans.push_back('0' + r);

    ans.append(num - ans.size(), '0');

    return ans;
  }
};
