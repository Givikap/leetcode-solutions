import heapq


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        if a:
            heap.append((-a, "a"))
        if b:
            heap.append((-b, "b"))
        if c:
            heap.append((-c, "c"))

        heapq.heapify(heap)

        currCount = 0
        prevLetter = " "

        happyString = []

        while heap:
            count, letter = heapq.heappop(heap)

            if currCount == 2 and letter == prevLetter:
                if not heap:
                    break

                t = (count, letter)
                count, letter = heapq.heappop(heap)
                heapq.heappush(heap, t)

            happyString.append(letter)

            currCount = currCount + 1 if letter == prevLetter else 1
            prevLetter = letter

            if count + 1 < 0:
                heapq.heappush(heap, (count + 1, letter))

        return "".join(happyString)
