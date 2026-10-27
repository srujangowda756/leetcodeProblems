class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        time = []

        for p, s in cars:
            time.append((target - p) / s)
        count = cur = 0

        for t in time:
            if t > cur:
                count += 1
                cur = t

        return count