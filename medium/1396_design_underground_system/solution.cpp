#include <string>
#include <unordered_map>

class UndergroundSystem {
public:
  UndergroundSystem() {
    system = std::unordered_map<int, std::pair<std::string, int>>();
    travels = std::unordered_map<
        std::string, std::unordered_map<std::string, std::pair<int, int>>>();
  }

  void checkIn(int id, std::string stationName, int t) {
    system[id] = {stationName, t};
  }

  void checkOut(int id, std::string stationName, int t) {
    const auto &[startStation, startTime] = system[id];

    auto &[sum, count] = travels[startStation][stationName];
    sum += t - startTime;
    ++count;

    system.erase(id);
  }

  double getAverageTime(std::string startStation, std::string endStation) {
    const auto &[sum, count] = travels[startStation][endStation];
    return static_cast<double>(sum) / static_cast<double>(count);
  }

private:
  std::unordered_map<int, std::pair<std::string, int>> system;
  std::unordered_map<std::string,
                     std::unordered_map<std::string, std::pair<int, int>>>
      travels;
};
