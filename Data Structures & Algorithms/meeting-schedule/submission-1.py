"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        inter = []
        for i in range(len(intervals)):
            inter.append([intervals[i].start, intervals[i].end])
        inter.sort()

        for i in range(len(inter) - 1):
            if (inter[i][1] > inter[i + 1][0]):
                return False
        return True