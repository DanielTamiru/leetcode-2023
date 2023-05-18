from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        interval_tuples = [tuple(interval) for interval in intervals]
        interval_tuples.sort()

        result = []
        cur_interval = interval_tuples[0] 

        for next_interval in interval_tuples[1:]:
            if next_interval[0] <= cur_interval[1]: # overlaps
                cur_interval = (cur_interval[0], max(cur_interval[1], next_interval[1]))
            else: # no overlap
                result.append(cur_interval)
                cur_interval = next_interval
        result.append(cur_interval) # append last interval

        return result
