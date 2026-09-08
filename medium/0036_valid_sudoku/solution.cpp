#include <vector>

class Solution {
public:
  bool isValidSudoku(std::vector<std::vector<char>> &board) {
    std::vector<std::vector<bool>> rowsMap(9, std::vector<bool>(9, false));
    std::vector<std::vector<bool>> colsMap(9, std::vector<bool>(9, false));
    std::vector<std::vector<bool>> boxesMap(9, std::vector<bool>(9, false));

    for (size_t row{}; row < 9; ++row) {
      for (size_t col{}; col < 9; ++col) {
        if (board[row][col] == '.')
          continue;

        size_t di = static_cast<size_t>(board[row][col] - '0' - 1);
        if (rowsMap[row][di] || colsMap[col][di])
          return false;

        size_t bi = 3 * (row / 3) + col / 3;
        if (boxesMap[bi][di])
          return false;

        rowsMap[row][di] = true;
        colsMap[col][di] = true;
        boxesMap[bi][di] = true;
      }
    }

    return true;
  }
};
