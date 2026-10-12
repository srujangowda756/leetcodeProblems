class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        new = sorted(intervals, key=lambda x: x[0])
        end = new[0][1]
        count = 0
        for i in range(1, len(new)):
            item = new[i]
            if item[0] < end:
                count += 1
                end = min(end, item[1])
            else:
                end = item[1]
        return count
        