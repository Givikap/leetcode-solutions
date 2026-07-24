#include <vector>

class Solution {
public:
  std::vector<std::vector<int>>
  merge(std::vector<std::vector<int>> &intervals) {
    std::sort(intervals.begin(), intervals.end());

    std::vector<std::vector<int>> mergedIntervals{intervals[0]};

    for (size_t i = 1; i < intervals.size(); ++i) {
      if (mergedIntervals.back()[1] >= intervals[i][0] &&
          mergedIntervals.back()[1] <= intervals[i][1])
        mergedIntervals.back()[1] = intervals[i][1];
      else if (mergedIntervals.back()[0] <= intervals[i][0] &&
               mergedIntervals.back()[1] >= intervals[i][1])
        continue;
      else
        mergedIntervals.push_back(intervals[i]);
    }

    return mergedIntervals;
  }
};
