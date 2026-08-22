#include <vector>

class Solution {
public:
  int maximalSquare(std::vector<std::vector<char>> &matrix) {
    const size_t rows = matrix.size();
    const size_t cols = matrix[0].size();

    std::vector<std::vector<int>> dp(rows, std::vector<int>(cols, 0));

    int maxSize = 0;

    for (size_t row{}; row < rows; ++row) {
      for (size_t col{}; col < cols; ++col) {
        if (row == 0 || col == 0 || matrix[row][col] == '0')
          dp[row][col] = matrix[row][col] - '0';
        else
          dp[row][col] = std::min({dp[row - 1][col - 1], dp[row - 1][col],
                                   dp[row][col - 1]}) +
                         1;

        maxSize = std::max(maxSize, dp[row][col]);
      }
    }

    return maxSize * maxSize;
  }
};
