#include <algorithm>
#include <string>
#include <unordered_map>
#include <vector>

class TimeMap {
public:
  TimeMap() {
    timestampsMap = std::unordered_map<std::string, std::vector<int>>();
    valuesMap = std::unordered_map<int, std::string>();
  }

  void set(std::string key, std::string value, int timestamp) {
    timestampsMap[key].push_back(timestamp);
    valuesMap[timestamp] = value;
  }

  std::string get(std::string key, int timestamp) {
    if (timestampsMap.find(key) == timestampsMap.end())
      return "";

    auto it = std::lower_bound(timestampsMap[key].begin(),
                               timestampsMap[key].end(), timestamp);

    if (it != timestampsMap[key].end() && *it <= timestamp)
      return valuesMap[*it];
    else if (it == timestampsMap[key].end() ||
             (it != timestampsMap[key].begin() && *it > timestamp))
      return valuesMap[*(it - 1)];
    else
      return "";
  }

private:
  std::unordered_map<std::string, std::vector<int>> timestampsMap;
  std::unordered_map<int, std::string> valuesMap;
};
