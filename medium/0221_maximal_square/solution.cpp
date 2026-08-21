#include <vector>

class Solution {
public:
  int maximalSquare(std::vector<std::vector<char>> &matrix) {
    const size_t rows = matrix.size();
    const size_t cols = matrix[0].size();

    std::vector<std::vector<int>> zerosCountsMap(rows,
                                                 std::vector<int>(cols, 0));

    for (size_t row{}; row < rows; ++row) {
      int rowZerosCount = 0;

      for (size_t col{}; col < cols; ++col) {
        zerosCountsMap[row][col] =
            (rowZerosCount += static_cast<int>(matrix[row][col] == '0'));

        if (row - 1 != -1)
          zerosCountsMap[row][col] += zerosCountsMap[row - 1][col];
      }
    }

    int maxSize = 0;

    for (size_t row{}; row < rows; ++row) {
      for (size_t col{}; col < cols; ++col) {
        if (matrix[row][col] == '1') {
          size_t r = row, c = col;
          while (true) {
            if (zerosCountsMap[r][c] -
                    (row - 1 != -1 ? zerosCountsMap[row - 1][c] : 0) -
                    (col - 1 != -1 ? zerosCountsMap[r][col - 1] : 0) +
                    (row - 1 != -1 && col - 1 != -1
                         ? zerosCountsMap[row - 1][col - 1]
                         : 0) ==
                0)
              maxSize = std::max(maxSize, static_cast<int>(r - row + 1));

            if (r + 1 == rows || c + 1 == cols || matrix[r + 1][c + 1] == '0')
              break;

            ++r;
            ++c;
          }
        }
      }
    }

    return maxSize * maxSize;
  }
};
