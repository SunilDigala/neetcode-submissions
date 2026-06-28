"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        prev_max = 0
        intervals.sort(key = lambda i : i.start)
        for i in intervals:
            current_min = i.start
            current_max = i.end

            if prev_max > current_min:
                return False
            
            prev_max = current_max
            prev_min = current_min
        return True
