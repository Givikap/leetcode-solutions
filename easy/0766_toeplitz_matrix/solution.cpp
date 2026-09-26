#include <vector>

class Solution {
public:
  bool isToeplitzMatrix(std::vector<std::vector<int>> &matrix) {
    const size_t rows = matrix.size();
    const size_t cols = matrix[0].size();

    for (size_t row = 0; row < rows; ++row) {
      size_t r = row;
      size_t c = 0;

      while (r < rows && c < cols) {
        if (matrix[r++][c++] != matrix[row][0])
          return false;
      }
    }

    for (size_t col = 1; col < cols; ++col) {
      size_t r = 0;
      size_t c = col;

      while (r < rows && c < cols) {
        if (matrix[r++][c++] != matrix[0][col])
          return false;
      }
    }

    return true;
  }
};
