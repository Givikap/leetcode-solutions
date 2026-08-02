#include <queue>
#include <string>

class Solution {
public:
  std::string longestDiverseString(int a, int b, int c) {
    std::priority_queue<std::pair<int, char>> pq;
    if (a)
      pq.push({a, 'a'});
    if (b)
      pq.push({b, 'b'});
    if (c)
      pq.push({c, 'c'});

    int currCount = 0;
    char prevLetter = ' ';

    std::string happyString;

    while (!pq.empty()) {
      auto p = pq.top();
      pq.pop();

      int count = p.first;
      char letter = p.second;

      if (currCount == 2 && letter == prevLetter) {
        if (pq.empty())
          break;

        count = pq.top().first;
        letter = pq.top().second;

        pq.pop();
        pq.push(p);
      }

      happyString.push_back(letter);

      currCount = (letter == prevLetter) ? currCount + 1 : 1;
      prevLetter = letter;

      if (count - 1 > 0)
        pq.push({count - 1, letter});
    }

    return happyString;
  }
};
