class Solution:
    def averageWaitingTime(self, customers: list[list[int]]) -> float:
        curr_time = customers[0][0]
        waiting_time = 0

        for arrival, time in customers:
            if arrival > curr_time:
                curr_time = arrival

            curr_time += time
            waiting_time += curr_time - arrival

        return waiting_time / len(customers)
