#include <unordered_map>
#include <vector>

class Solution {
public:
  int minimumDistance(std::vector<int> &nums) {
    std::unordered_map<int, std::vector<size_t>> indicesMap;

    for (size_t i = 0; i < nums.size(); ++i)
      indicesMap[nums[i]].push_back(i);

    int minDist = INT_MAX;

    for (const auto &[_, indices] : indicesMap) {
      if (indices.size() >= 3) {
        for (size_t i = 0; i < indices.size() - 2; ++i)
          minDist = std::min(minDist, 2 * (int)(indices[i + 2] - indices[i]));
      }
    }

    return minDist == INT_MAX ? -1 : minDist;
  }
};
