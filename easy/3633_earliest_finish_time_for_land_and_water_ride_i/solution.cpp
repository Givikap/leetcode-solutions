#include <vector>

class Solution {
public:
  int earliestFinishTime(std::vector<int> &landStartTime,
                         std::vector<int> &landDuration,
                         std::vector<int> &waterStartTime,
                         std::vector<int> &waterDuration) {
    int earliestLandFinishTime = INT_MAX;
    for (size_t i = 0; i < landStartTime.size(); ++i)
      earliestLandFinishTime =
          std::min(earliestLandFinishTime, landStartTime[i] + landDuration[i]);

    int earliestWaterFinishTime = INT_MAX;
    int earliestFinishTime = INT_MAX;

    for (size_t i = 0; i < waterStartTime.size(); ++i) {
      earliestWaterFinishTime = std::min(earliestWaterFinishTime,
                                         waterStartTime[i] + waterDuration[i]);
      earliestFinishTime =
          std::min(earliestFinishTime,
                   std::max(earliestLandFinishTime, waterStartTime[i]) +
                       waterDuration[i]);
    }

    for (size_t i = 0; i < landStartTime.size(); ++i)
      earliestFinishTime =
          std::min(earliestFinishTime,
                   std::max(earliestWaterFinishTime, landStartTime[i]) +
                       landDuration[i]);

    return earliestFinishTime;
  }
};
