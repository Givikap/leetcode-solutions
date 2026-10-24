#include <cstdlib>
#include <string>
#include <vector>

class Solution {
public:
  int countDaysTogether(std::string arriveAlice, std::string leaveAlice,
                        std::string arriveBob, std::string leaveBob) {
    const std::vector<int> daysInMonth = {31, 28, 31, 30, 31, 30,
                                          31, 31, 30, 31, 30, 31};

    int arriveAliceMonth = stoi(arriveAlice.substr(0, 2));
    int arriveAliceDay = stoi(arriveAlice.substr(3, 2));

    int arriveBobMonth = stoi(arriveBob.substr(0, 2));
    int arriveBobDay = stoi(arriveBob.substr(3, 2));

    int togetherStartMonth;
    int togetherStartDay;

    if (arriveAliceMonth == arriveBobMonth) {
      togetherStartMonth = arriveAliceMonth;
      togetherStartDay = std::max(arriveAliceDay, arriveBobDay);
    } else {
      togetherStartMonth = std::max(arriveAliceMonth, arriveBobMonth);
      togetherStartDay =
          arriveAliceMonth > arriveBobMonth ? arriveAliceDay : arriveBobDay;
    }

    int leaveAliceMonth = stoi(leaveAlice.substr(0, 2));
    int leaveAliceDay = stoi(leaveAlice.substr(3, 2));

    int leaveBobMonth = stoi(leaveBob.substr(0, 2));
    int leaveBobDay = stoi(leaveBob.substr(3, 2));

    int togetherEndMonth;
    int togetherEndDay;

    if (leaveAliceMonth == leaveBobMonth) {
      togetherEndMonth = leaveAliceMonth;
      togetherEndDay = std::min(leaveAliceDay, leaveBobDay);
    } else {
      togetherEndMonth = std::min(leaveAliceMonth, leaveBobMonth);
      togetherEndDay =
          leaveAliceMonth < leaveBobMonth ? leaveAliceDay : leaveBobDay;
    }

    int daysCount = 0;
    if (togetherStartMonth > togetherEndMonth ||
        (togetherStartMonth == togetherEndMonth &&
         togetherStartDay > togetherEndDay))
      return daysCount;

    while (togetherStartMonth < togetherEndMonth)
      daysCount += daysInMonth[static_cast<size_t>(togetherStartMonth++ - 1)];

    return daysCount + togetherEndDay - togetherStartDay + 1;
  }
};
