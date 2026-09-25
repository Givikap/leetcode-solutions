class Solution:
    def readBinaryWatch(self, turned_on: int) -> list[str]:
        if turned_on == 0:
            return ["0:00"]
        if turned_on > 8:
            return []

        times = []

        hours = [hour.bit_count() for hour in range(12)]
        minutes = [minute.bit_count() for minute in range(60)]

        for hour, hour_bit_count in enumerate(hours):
            if hour_bit_count <= turned_on:
                for minute, minute_bit_count in enumerate(minutes):
                    if hour_bit_count + minute_bit_count == turned_on:
                        times.append(f"{hour}:{minute:02d}")

        return times
