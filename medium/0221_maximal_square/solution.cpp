#include <vector>

class Solution {
public:
  int maximalSquare(std::vector<std::vector<char>> &matrix) {
    const size_t rows = matrix.size();
    const size_t cols = matrix[0].size();

    std::vector<int> dp(cols, 0);

    int prev = 0;
    int maxSize = 0;

    for (size_t row{}; row < rows; ++row) {
      for (size_t col{}; col < cols; ++col) {
        int temp = dp[col];

        if (row == 0 || col == 0 || matrix[row][col] == '0')
          dp[col] = matrix[row][col] - '0';
        else
          dp[col] = std::min({prev, dp[col], dp[col - 1]}) + 1;

        prev = temp;
        maxSize = std::max(maxSize, dp[col]);
      }
    }

    return maxSize * maxSize;
  }
};
